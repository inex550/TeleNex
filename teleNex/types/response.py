from typing import List
from . import TeleObj, Field

from .update import Update


class Response(TeleObj):
    ok: bool = Field()
    result: List[Update] = Field(Update, parent=list)