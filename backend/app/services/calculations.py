from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from math import ceil
from random import Random

D = Decimal
MONEY = D("0.01")
def money(value: Decimal) -> Decimal: return value.quantize(MONEY, rounding=ROUND_HALF_UP)

@dataclass(frozen=True)
class ShouldCostInput:
    net_material_qty: Decimal; material_rate: Decimal; yield_rate: Decimal
    cycle_hours: Decimal; machine_rate: Decimal; labor_hours: Decimal; labor_rate: Decimal
    setup_cost: Decimal = D("0"); annual_volume: Decimal = D("1"); tooling: Decimal = D("0")
    amortization_volume: Decimal = D("1"); other_direct: Decimal = D("0")
    overhead_pct: Decimal = D("0"); margin_pct: Decimal = D("0"); risk_allowance: Decimal = D("0")

def should_cost(x: ShouldCostInput) -> dict:
    if not D("0") < x.yield_rate <= D("1") or x.annual_volume <= 0 or x.amortization_volume <= 0:
        raise ValueError("yield_rate must be (0,1] and volumes must be positive")
    material=x.net_material_qty*x.material_rate/x.yield_rate
    machine=x.cycle_hours*x.machine_rate; labor=x.labor_hours*x.labor_rate
    setup=x.setup_cost/x.annual_volume; tooling=x.tooling/x.amortization_volume
    subtotal=material+machine+labor+setup+tooling+x.other_direct
    overhead=subtotal*x.overhead_pct; profit=(subtotal+overhead)*x.margin_pct
    total=subtotal+overhead+profit+x.risk_allowance
    return {k:money(v) for k,v in {"material":material,"machine":machine,"labor":labor,"setup":setup,"tooling":tooling,"other_direct":x.other_direct,"overhead":overhead,"profit":profit,"risk_allowance":x.risk_allowance,"total":total}.items()}

DEFAULT_RISK_WEIGHTS={"delivery":D(".15"),"quality":D(".15"),"capacity":D(".10"),"financial":D(".10"),"geopolitical":D(".10"),"single_source":D(".10"),"lead_time":D(".10"),"commodity":D(".05"),"commercial":D(".05"),"compliance":D(".05"),"continuity":D(".05")}
def risk_score(dimensions: dict[str, Decimal|None], weights=DEFAULT_RISK_WEIGHTS) -> dict:
    present={k:D(str(v)) for k,v in dimensions.items() if v is not None and k in weights}
    for value in present.values():
        if not 0 <= value <= 100: raise ValueError("risk dimensions must be 0..100")
    covered=sum(weights[k] for k in present); score=sum(present[k]*weights[k] for k in present)/covered if covered else None
    rounded=money(score) if score is not None else None
    band=None if score is None else "Low" if score<25 else "Moderate" if score<50 else "High" if score<70 else "Critical"
    return {"score":rounded,"band":band,"completeness":money(covered*100),"missing":[k for k in weights if k not in present],"contributions":{k:money(present[k]*weights[k]/covered) for k in present}}

def disruption_cost(probability: Decimal, downtime_days: Decimal, daily_impact: Decimal, dependency: Decimal) -> Decimal:
    if any(v<0 for v in (probability,downtime_days,daily_impact,dependency)): raise ValueError("inputs cannot be negative")
    return money(probability*downtime_days*daily_impact*dependency)

AWARD_WEIGHTS={"landed_cost":D(".30"),"quality":D(".15"),"delivery":D(".15"),"capacity":D(".10"),"technical":D(".10"),"supplier_risk":D(".10"),"lead_time":D(".05"),"terms":D(".05")}
def award_score(scores: dict[str, Decimal], weights=AWARD_WEIGHTS) -> dict:
    if set(scores)!=set(weights): raise ValueError("all award dimensions are required")
    total=sum(D(str(scores[k]))*weights[k] for k in weights)
    return {"score":money(total),"contributions":{k:money(D(str(scores[k]))*weights[k]) for k in weights}}

def monte_carlo(base_spend: Decimal, iterations=5000, seed=2026, volatility=.10) -> dict:
    if iterations<100: raise ValueError("iterations must be at least 100")
    rng=Random(seed); outcomes=sorted(float(base_spend)*max(0,rng.gauss(1,volatility)) for _ in range(iterations))
    return {"seed":seed,"iterations":iterations,"p10":money(D(str(outcomes[ceil(iterations*.10)-1]))),"p50":money(D(str(outcomes[ceil(iterations*.50)-1]))),"p90":money(D(str(outcomes[ceil(iterations*.90)-1])))}
