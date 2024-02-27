from pydantic import BaseModel
from typing import List, Optional
from . import Info

class Origin(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None

class Location(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None

class Character(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    status: Optional[str] = None
    species: Optional[str] = None
    type: Optional[str] = None
    gender: Optional[str] = None
    origin: Optional[Origin] = None
    location: Optional[Location] = None
    image: Optional[str] 
    episode: Optional[List[str]] = None
    url: Optional[str] = None
    created: Optional[str] = None


class ResponseCharacter(BaseModel):
    info: Info
    results: List[Character]