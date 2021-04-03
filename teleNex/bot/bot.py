from typing import Callable, Optional, Any

from .helpers import generate_payload
from .base import BaseBot
from ..types import Message, File

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
    ) -> Message:
        data = generate_payload(locals().copy())
        response = await self.api.make_request('sendMessage', data)
        return self._process_response(response, Message)

    async def download_file(self, file_id: str, save_path: str=None):
        file: File = await self.get_file(file_id)
        return await self.api.download_file(file.file_path, save_path)

    async def get_file(self, file_id: str):
        data = { 'file_id': file_id }
        response = await self.api.make_request('getFile', data=data)
        return self._process_response(response, File)

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
