from typing import List, Optional

from . import ReplyBase
from .. import TeleObj, Field
from ...helpers import generate_payload


class KeyboardButton(TeleObj):
    text: str = Field()
    request_contact: Optional[bool] = Field()
    request_location: Optional[bool] = Field()

    def __init__(self, 
        text: str, 
        request_contact: Optional[bool]=None, 
        request_location: Optional[bool]=None
    ):
        payload = generate_payload(locals().copy())
        super().__init__(payload)


class ReplyKeyboardMarkup(ReplyBase):
    keyboard: List[List[KeyboardButton]] = Field(KeyboardButton, two_dim=True)
    resize_keyboard: Optional[bool] = Field()
    one_time_keyboard: Optional[bool] = Field()
    selective: Optional[bool] = Field()

    def __init__(
        self, 
        keyboard: List[List[KeyboardButton]],
        resize_keyboard: Optional[bool] = None, 
        one_time_keyboard: Optional[bool] = None,
        selective: Optional[bool] = None
    ):
        payload = generate_payload(locals().copy())
        super().__init__(payload)
