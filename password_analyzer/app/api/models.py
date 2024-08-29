# app/api/models.py

from pydantic import BaseModel, Field

class PasswordAnalysisRequest(BaseModel):
    password: str = Field(..., min_length=1, description="Password to analyze")

class PasswordAnalysisResponse(BaseModel):
    score: int = Field(..., ge=0, le=10, description="Password strength score (0-10)")
    strength: str = Field(..., description="calculated strength score")
    feedback: list = Field(..., description="Feedback on password strength")

class PasswordGenerationRequest(BaseModel):
    length: int = Field(default=12, ge=8, le=128, description="Password length")
    include_uppercase: bool = Field(default=True, description="Include uppercase letters")
    include_lowercase: bool = Field(default=True, description="Include lowercase letters")
    include_numbers: bool = Field(default=True, description="Include numbers")
    include_special: bool = Field(default=True, description="Include special characters")

class PasswordGenerationResponse(BaseModel):
    password: str = Field(..., description="Generated password")

class ErrorResponse(BaseModel):
    detail: str = Field(..., description="Error message")    