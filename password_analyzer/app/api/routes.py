# app/api/routes.py

from fastapi import APIRouter, HTTPException
from api.models import (
    PasswordAnalysisRequest, 
    PasswordAnalysisResponse, 
    PasswordGenerationRequest, 
    PasswordGenerationResponse, 
    ErrorResponse
)
from services import password_analyzer, password_generator
from typing import Union

router = APIRouter()

@router.post("/analyze-password", response_model=Union[PasswordAnalysisResponse, ErrorResponse])
async def analyze_password(request: PasswordAnalysisRequest):
    try:
        result = password_analyzer.analyze_password(request.password)
        return PasswordAnalysisResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/generate-password", response_model=Union[PasswordGenerationResponse, ErrorResponse])
async def generate_password(request: PasswordGenerationRequest):
    try:
        password = password_generator.generate_password(
            request.length, 
            request.include_uppercase, 
            request.include_lowercase, 
            request.include_numbers, 
            request.include_special
        )
        return PasswordGenerationResponse(password=password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))