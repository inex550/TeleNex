from typing import Optional
from . import TeleObj, Field

from .user import User


class MessageEntity(TeleObj):
    type: str = Field()
    offset: int = Field()
    length: int = Field()
    url: Optional[str] = Field()
    user: Optional[User] = Field(User)
    language: Optional[str] = Field()