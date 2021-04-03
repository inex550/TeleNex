from typing import Any, Dict, Callable, List

from ..types import Update, Message, Response
from .helpers import ApiHelper

import asyncio


class BaseBot:
    def __init__(self, token: str) -> None:
        self.token = token

        self.api = ApiHelper(token)

        self._update_offset = 0

        self._key_text_msgs: Dict[str, Callable[[Message], Any]] = {}
        self._global_msg_types: Dict[str, Callable[[Message], Any]] = {}

    async def _process_message(self, message: Message):
        if 'all' in self._global_msg_types:
            asyncio.create_task( self._global_msg_types['all'](message) )

        if message.text:
            if 'text' in self._global_msg_types:
                asyncio.create_task( self._global_msg_types['text'](message) )

            if message.text in self._key_text_msgs:
                asyncio.create_task( self._key_text_msgs[message.text](message) )

        if message.document:
            if 'document' in self._global_msg_types:
                asyncio.create_task( self._global_msg_types['document'](message) )

        if message.photo:
            if 'photo' in self._global_msg_types:
                asyncio.create_task( self._global_msg_types['photo'](message) )

    async def _process_update(self, update: Update) -> None:
        if update.message:
            await self._process_message(update.message)
        else:
            assert False, f'update attributes not supported'

    def _process_response(self, json_data: dict, cls):
        response = Response(json_data)
        if response.ok:
            return response.result_instance(cls)
        else:
            assert False, f'{response.error_code} {response.description}'
        

    async def polling(self):
        async with self.api.session:
            while True:
                json_data = await self.api.get_updates(timeout=60, offset=self._update_offset)
                updates: List[Update] = self._process_response(json_data, Update)

                for update in updates:
                    self._update_offset = update.update_id + 1
                    await self._process_update(update)