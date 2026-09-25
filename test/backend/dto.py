from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, Field

class ModelInfo(BaseModel):
    id: str
    huggingface_id: str

class ModelsResponse(BaseModel):
    models: List[ModelInfo]
