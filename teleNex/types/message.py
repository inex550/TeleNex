from typing import Optional, List
from . import TeleObj, Field

from .user import User
from .chat import Chat
from .message_entity import MessageEntity
from .document import Document
from .photo_size import PhotoSize


class Message(TeleObj):
    _corrects = {
        'from': 'from_user'
    }

    message_id: int = Field()
    from_user: Optional[User] = Field(User)
    sender_chat: Optional[Chat] = Field(Chat)
    date: int = Field()
    chat: Chat = Field(Chat)
    forward_from: Optional[User] = Field(User)
    forward_from_chat: Optional[Chat] = Field(Chat)
    forward_from_message_id: Optional[int] = Field()
    forward_signature: Optional[str] = Field()
    forward_sender_name: Optional[str] = Field()
    forward_date: Optional[int] = Field()
    reply_to_message: Optional['Message'] = Field(...)
    via_bot: Optional[User] = Field(User)
    edit_date: Optional[int] = Field()
    media_group_id: Optional[str] = Field()
    author_signature: Optional[str] = Field()
    text: Optional[str] = Field()
    entities: Optional[List[MessageEntity]] = Field(MessageEntity, parent=list)
    document: Optional[Document] = Field(Document)
    photo: Optional[List[PhotoSize]] = Field(PhotoSize, parent=list)