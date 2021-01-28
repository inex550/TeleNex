from typing import Optional
from . import TeleObj, Field


class Chat(TeleObj):
    id: int = Field()
    type: str = Field()
    title: Optional[str] = Field()
    username: Optional[str] = Field()
    first_name: Optional[str] = Field()
    last_name: Optional[str] = Field()
    bio: Optional[str] = Field()
    description: Optional[str] = Field()
    invite_link: Optional[str] = Field()