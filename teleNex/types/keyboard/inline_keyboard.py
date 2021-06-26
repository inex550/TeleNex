from typing import Optional, List

from .. import Field, TeleObj, LoginUrl
from ...helpers import generate_payload

from . import ReplyBase


class InlineKeyboardButton(TeleObj):
    text                            : str = Field()
    url                             : Optional[str] = Field()
    login_url                       : Optional[LoginUrl] = Field(LoginUrl)
    callback_data                   : Optional[str] = Field()
    switch_inline_query             : Optional[str] = Field()
    switch_inline_query_current_chat: Optional[str] = Field()
    pay                             : Optional[bool] = Field()

    def __init__(
        self,
        text                            : str,
        url                             : Optional[str] = None,
        login_url                       : Optional[LoginUrl] = None,
        callback_data                   : Optional[str] = None,
        switch_inline_query             : Optional[str] = None,
        switch_inline_query_current_chat: Optional[str] = None,
        pay                             : Optional[bool] = None,
    ):
        data = generate_payload(locals().copy())
        super().__init__(data)


class InlineKeyboardMarkup(ReplyBase):
    inline_keyboard: List[List[InlineKeyboardButton]] = Field(InlineKeyboardButton, two_dim=True)

    def __init__(
        self,
        inline_keyboard: List[List[InlineKeyboardButton]]
    ):
        data = generate_payload(locals().copy())
        super().__init__(data)