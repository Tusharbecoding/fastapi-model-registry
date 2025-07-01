import json
import aiofiles
import os
from typing import Optional, List, Dict, Any
from datetime import datetime
import uuid
from .models import ModelResponse, ModelCreate, ModelUpdate, ModelStatus

class JSONDatabase:
    def __init__(self, db_path: str = "../data/models.json"):
        self.db_path = db_path
        self.ensure_db_exists()

    def ensure_db_exists(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w') as f:
                json.dump([], f)

    async def read_all_models(self) -> List[Dict[str, Any]]:
        try:
            async with aiofiles.open(self.db_path, 'r') as f:
                content = await f.read()
                return json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    async def write_all_models(self, models: List[Dict[str, Any]]) -> None:
        async with aiofiles.open(self.db_path, 'w') as f:
            await f.write(json.dumps(models, indent=2, default=str))
            
