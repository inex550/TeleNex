from typing import Callable, Optional, Any

from .helpers import generate_payload
from .base import BaseBot
from ..types import Message

import asyncio


class Bot(BaseBot):
    async def send_msg(
        self,
        chat_id: Optional[int],
        text: str,
        parse_mode: Optional[str] = None, 
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[int] = None
    ):
        data = generate_payload(locals().copy())
        response = await self.api.make_request('sendMessage', data)
        self._process_response(response)

    def on_message(
        self, *,
        text: str = None,
        msg_type: str = None
    ):
        def decorator(func: Callable[[Message], Any]):
            if text:
                self._key_text_msgs[text] = func
            
            if msg_type:
                self._global_msg_types[msg_type] = func

        return decorator
            
    def run(
        self,
        polling = True
    ):
        if polling:
            try:
                asyncio.run(self.polling())
            except KeyboardInterrupt:
                quit()

        assert polling, 'polling must be True'
