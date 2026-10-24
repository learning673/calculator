
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.calculator import calculate
from backend.schemas import (
    CalculationRequest,
    CalculationResponse,
)

app = FastAPI(title="Full-Stack Calculator API")

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static",
)

@app.get("/")
def home():
    return FileResponse(FRONTEND_DIR / "index.html")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post(
    "/api/calculate",
    response_model=CalculationResponse,
)
def calculate_endpoint(
    request: CalculationRequest,
):
    try:
        result = calculate(
            request.a,
            request.b,
            request.operation,
        )
        return CalculationResponse(result=result)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc
