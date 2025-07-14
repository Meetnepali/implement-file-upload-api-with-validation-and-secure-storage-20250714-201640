from pydantic import BaseModel, Field
from typing import Optional

class UserProfileUpdate(BaseModel):
    username: str = Field(..., example="john_doe")
    bio: Optional[str] = Field(None, example="Nature lover and hiker.")

class UserProfileResponse(BaseModel):
    username: str
    bio: Optional[str]
    avatar_url: Optional[str]

class ErrorResponse(BaseModel):
    error: str
    details: Optional[str]
