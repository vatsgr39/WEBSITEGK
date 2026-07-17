from decimal import Decimal
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel, Field
from uuid import uuid4
from .services.calculations import ShouldCostInput, award_score, disruption_cost, risk_score, should_cost

app=FastAPI(title="SOURCE TWIN AI API",version="0.1.0",docs_url="/docs")
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:3000"],allow_credentials=True,allow_methods=["GET","POST"],allow_headers=["Authorization","Content-Type","X-Request-ID"])
@app.middleware("http")
async def request_context(request:Request,call_next):
    rid=request.headers.get("x-request-id",str(uuid4())); response=await call_next(request); response.headers["X-Request-ID"]=rid; response.headers["X-Content-Type-Options"]="nosniff"; response.headers["Referrer-Policy"]="strict-origin-when-cross-origin"; return response
@app.get("/health")
def health(): return {"status":"ok"}
@app.get("/ready")
def ready(): return {"status":"ready","database":"configured"}
@app.get("/metrics",response_class=PlainTextResponse)
def metrics(): return "# HELP source_twin_up Service health\n# TYPE source_twin_up gauge\nsource_twin_up 1\n"

class RiskRequest(BaseModel): dimensions:dict[str,Decimal|None]
@app.post("/api/v1/risk/calculate")
def calculate_risk(body:RiskRequest): return risk_score(body.dimensions)
class DisruptionRequest(BaseModel): probability:Decimal=Field(ge=0,le=1); downtime_days:Decimal=Field(ge=0); daily_impact:Decimal=Field(ge=0); dependency:Decimal=Field(ge=0,le=1)
@app.post("/api/v1/scenarios/disruption")
def calculate_disruption(body:DisruptionRequest): return {"expected_disruption_cost":disruption_cost(body.probability,body.downtime_days,body.daily_impact,body.dependency)}
@app.get("/api/v1/dashboard")
def dashboard(): return {"addressable_spend":48200000,"annualized_savings":3740000,"active_rfqs":18,"high_risk_suppliers":7,"average_otif":94.2,"model_version":"risk-v2.4"}
@app.get("/api/v1/rfqs/RFQ-2026-001/recommendation")
def recommendation(): return {"primary":{"supplier_id":"SUP-1014","name":"Northstar Fabrication","split":70},"secondary":{"supplier_id":"SUP-1022","name":"Great Lakes Precision","split":30},"confidence":.91,"citations":["Supplier SUP-1014","RFQ RFQ-2026-001","Component CMP-001"],"reason":"Best risk-adjusted value despite a 6.5% quoted-price premium."}
