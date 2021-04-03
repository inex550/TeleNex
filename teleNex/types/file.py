from typing import Optional
from . import TeleObj, Field


class File(TeleObj):
    file_id: str = Field()
    file_unique_id: str = Field()
    file_size: Optional[str] = Field()
    file_path: Optional[str] = Field()