from typing import Callable, Optional, Any, List

from ..helpers import generate_payload
from .base import BaseBot
from ..types import (
    Message, 
    File,
    ReplyBase,
)
from ..types import ReplyBase

import asyncio
from asyncio import Queue


class Bot(BaseBot):
    async def send_msg(
        self,
        chat_id                     : int,
        text                        : str,
        parse_mode                  : Optional[str] = None, 
        disable_web_page_preview    : Optional[bool] = None,
        disable_notification        : Optional[bool] = None,
        reply_to_message_id         : Optional[int] = None,
        allow_sending_without_reply : Optional[int] = None,
        reply_markup                : Optional[ReplyBase] = None
    ) -> Message:
        data = generate_payload(locals().copy())
        response = await self._api.make_request('sendMessage', data)
        return self._process_response(response, Message)


    async def send_sticker(
        self,
        chat_id                     : int,
        sticker                     : str,
        disable_notification        : Optional[bool] = None,
        reply_to_message_id         : Optional[int] = None,
        allow_sending_without_reply : Optional[int] = None,
        reply_markup                : Optional[ReplyBase] = None
    ):
        data = generate_payload(locals().copy())
        response = await self._api.make_request('sendSticker', data)
        return self._process_response(response, Message)


    async def download_file(self, file_id: str, save_path: str=None):
        file: File = await self.get_file(file_id)
        return await self._api.download_file(file.file_path, save_path)


    async def get_file(self, file_id: str):
        data = { 'file_id': file_id }
        response = await self._api.make_request('getFile', data=data)
        return self._process_response(response, File)


    async def send_question(
        self,
        chat_id: str,
        text: str,
    ) -> Message:
        await self.send_msg(chat_id, text)

        queue = self.question_queues.get(chat_id);
        if queue is not None:
            queue.put_nowait(None)
        queue = self.question_queues[chat_id] = Queue()

        msg: Message = await queue.get()
        self.question_queues[chat_id] = None
        return msg


    def on_message(
        self, *,
        texts   : List[str] = None,
        cmds    : List[str] = None,
        stickers: List[str] = None,
        msg_type: str = None,
        func    : Callable[[Message], bool] = None
    ):
        def decorator(d_func: Callable[[Message], Any]):
            if texts:
                self._key_text_msgs.update( {text: d_func for text in texts} )

            if cmds:
                self._key_cmd_msgs.update( {cmd: d_func for cmd in cmds} )

            if stickers:
                self._file_id_sticker_msgs.update( {sticker: d_func for sticker in stickers} )
            
            if msg_type:
                self._global_msg_types[msg_type] = d_func

            if func:
                self._func_handlers.append( (func, d_func) )

        return decorator

            
    def run(self):
        try:
            asyncio.run(self.polling())
        except KeyboardInterrupt:
            quit()
