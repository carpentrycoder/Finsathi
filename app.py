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
    goals: list = []

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

#get apis 

@app.get("/risk-profile")
def get_risk_profile(
    age: int,
    income: float,
    expenses: float,
    savings: float,
    dependents: int,
    risk_tolerance: str
):
    return {
        "risk_category": risk_tolerance,
        "confidence": 0.82,
        "score": 0.68,
        "input": {
            "age": age,
            "income": income,
            "expenses": expenses,
            "savings": savings,
            "dependents": dependents,
            "risk_tolerance": risk_tolerance
        }
    }

@app.get("/goal-feasibility")
def get_goal_feasibility(
    goal_amount: float,
    time_horizon_months: int,
    monthly_surplus: float
):
    required = round(goal_amount / time_horizon_months, 2)

    return {
        "goal_feasible": required <= monthly_surplus,
        "required_monthly_investment": required,
        "recommended_strategy": "SIP + debt buffer",
        "alternative_timeline_months": (
            time_horizon_months + 6
            if required > monthly_surplus
            else time_horizon_months
        )
    }
