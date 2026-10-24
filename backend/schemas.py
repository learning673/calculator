
from typing import Literal
from pydantic import BaseModel, Field

class CalculationRequest(BaseModel):
    a: float = Field(allow_inf_nan=False)
    b: float = Field(allow_inf_nan=False)
    operation: Literal[
        "add", "subtract", "multiply", "divide"
    ]

class CalculationResponse(BaseModel):
    result: float
