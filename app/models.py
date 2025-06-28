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
