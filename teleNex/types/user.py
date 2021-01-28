from typing import Optional
from . import TeleObj, Field


class User(TeleObj):
    id: int = Field()
    is_bot: bool = Field()
    first_name: str = Field()
    last_name: Optional[str] = Field()
    username: Optional[str] = Field()
    language_code: Optional[str] = Field()
    can_join_groups: Optional[bool] = Field()
    can_read_all_group_messages: Optional[bool] = Field()
    supports_inline_queries: Optional[bool] = Field()
