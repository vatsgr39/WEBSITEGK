from decimal import Decimal as D
import pytest
from app.services.calculations import ShouldCostInput, award_score, disruption_cost, monte_carlo, risk_score, should_cost
def test_should_cost_fixed_expected_value():
    result=should_cost(ShouldCostInput(D("10"),D("2"),D(".8"),D(".5"),D("60"),D(".25"),D("32"),D("1000"),D("1000"),D("50000"),D("10000"),D("3"),D(".10"),D(".08"),D("1")))
    assert result["material"]==D("25.00") and result["total"]==D("86.54")
def test_missing_risk_is_not_zero():
    r=risk_score({"delivery":D("80"),"quality":None}); assert r["score"]==D("80.00") and "quality" in r["missing"] and r["completeness"]==D("15.00")
def test_risk_band_boundaries():
    assert risk_score({k:D("70") for k in ["delivery","quality","capacity","financial","geopolitical","single_source","lead_time","commodity","commercial","compliance","continuity"]})["band"]=="Critical"
def test_disruption_formula(): assert disruption_cost(D(".25"),D("20"),D("100000"),D(".8"))==D("400000.00")
def test_award_weights(): assert award_score({"landed_cost":D("80"),"quality":D("90"),"delivery":D("90"),"capacity":D("85"),"technical":D("95"),"supplier_risk":D("78"),"lead_time":D("84"),"terms":D("82")})["score"]==D("85.10")
def test_monte_carlo_reproducible(): assert monte_carlo(D("1000000"),500,42)==monte_carlo(D("1000000"),500,42)
