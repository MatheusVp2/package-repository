from pydantic import BaseModel
from typing import Optional

class Info(BaseModel):
    count: Optional[int] = None
    pages: Optional[int] = None
    next: Optional[str] = None
    prev: Optional[str] = None