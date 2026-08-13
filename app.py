from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RiskRequest(BaseModel):
    age: int
    income: float
    expenses: float
    savings: float
    dependents: int
    risk_tolerance: str

@app.post("/risk-profile")
def risk_profile(req: RiskRequest):
    return {"risk_category": req.risk_tolerance, "confidence": 0.82, "score": 0.68}

@app.post("/goal-feasibility")
def goal_feasibility(payload: dict):
    amt = payload["goal_amount"]
    months = payload["time_horizon_months"]
    surplus = payload["monthly_surplus"]
    required = round(amt / months, 2)
    return {
        "goal_feasible": required <= surplus,
        "required_monthly_investment": required,
        "recommended_strategy": "SIP + debt buffer",
        "alternative_timeline_months": months + 6 if required > surplus else months
    }
