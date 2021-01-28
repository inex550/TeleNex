from typing import Optional
from . import TeleObj, Field

from .message import Message


class Update(TeleObj):
    update_id: int = Field()
    message: Optional[Message] = Field(Message)
    edited_message: Optional[Message] = Field(Message)
    channel_post: Optional[Message] = Field(Message)
    edited_channel_post: Optional[Message] = Field(Message)
    