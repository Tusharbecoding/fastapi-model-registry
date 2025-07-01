from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class ModelStatus(str, Enum):
    ACTIVE = "active" 
    INACTIVE = "inactive"
    TRAINING = "training"
    DEPRICATED = "depricated"

class ModelType(str, Enum):
    CLASSIFICATION = "classification"
    REGRESSION = "regression"
    NLP = "nlp"
    COMPUTER_VISION = "computer_vision"
    GENERATIVE = "generative"

class ModelBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Model Name")
    description: str = Field(..., min_length=10, description="Description")
    model_type: ModelType = Field(..., description="Model types")
    tags: Optional[List[str]] = Field(default=[], description="Model Tags")

    @validator('tags')
    def validate_tags(cls, v):
        if len(v) > 10:
            raise ValueError("max 10 tags allowed")
        return [tag.lower().strip() for tag in v]

class ModelCreate(ModelBase):
    pass

class ModelUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=10)
    status: Optional[ModelStatus] = None
    tags: Optional[List[str]] = None


class ModelResponse(ModelBase):
    id: str = Field(..., description="Unique model id")
    status: ModelStatus = Field(default=ModelStatus.ACTIVE)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    file_path: Optional[str] = Field(None, description, "Path")
    metrics: Optional[Dict[str, float]] = Field(default={}, description="Model perf")


class Config:
    from_attributes = True
    json_schema_extra = {
        "example": {
            "id": "model_123",
            "name": "Image Classifier",
            "description": "CNN Model for classifying images",
            "model_type": "computer_vision",
            "status": "active",
            "tags": ["cnn", "pytorch", "production"],
            "metrics": {"accuracy": 0.95, "f1_score": 0.93}
        }
    }

class PredictionResponse(BaseModel):
    model_id: str
    prediction: Any = Field(..., description="Model prediction output")
    confidence: Optional[float] = Field(..., ge=0.0, le=1.0, description="Prediction")
    processing_time_ms: float = Field(..., description="Prediction time")

    
        
