from typing import Any, Dict, Callable

from ..types import Response, Update, Message
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
            await asyncio.create_task( self._global_msg_types['all'](message) )

        if message.text in self._key_text_msgs:
            await asyncio.create_task( self._key_text_msgs[message.text](message) )

            if 'text' in self._global_msg_types:
                await asyncio.create_task( self._global_msg_types['text'](message) )

        if message.document:
            if 'document' in self._global_msg_types:
                await asyncio.create_task( self._global_msg_types['document'](message) )

    async def _process_update(self, update: Update) -> None:
        if update.message:
            await self._process_message(update.message)
        else:
            assert False, f'update attributes not supported'

    def _process_response(self, response: dict):
        assert response.get('ok'), response

    async def polling(self):
        async with self.api.session:
            while True:
                json_data = await self.api.get_updates(timeout=60, offset=self._update_offset)

                response = Response(json_data)

                if response.ok:
                    for update in response.result:
                        self._update_offset = update.update_id + 1
                        await self._process_update(update)
                else:
                    assert False, 'ok is False'