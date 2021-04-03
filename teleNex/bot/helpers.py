from TeleNex.teleNex.types import chat
from typing import List, Optional

import aiohttp


def generate_payload(args: dict):
    del args['self']
    data = { k: v for k, v in args.items() if v is not None }

    return data

class ApiHelper:
    def __init__(self, token):
        self.token = token

        self._session: aiohttp.ClientSession = None

    @property
    def session(self):
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def make_request(self, method: str, data: dict = None) -> Optional[dict]:
        url = f'https://api.telegram.org/bot{self.token}/{method}'
        async with self.session.post(url, json=data) as resp:
            return await resp.json()

    async def download_file(self, file_path: str, save_path: str=None):
        async with self.session.get(f'https://api.telegram.org/file/bot{self.token}/{file_path}') as resp:
            if save_path:
                with open(save_path, 'wb') as file:
                    data = await resp.content.read()
                    file.write(data)
            else:
                return await resp.content.read()

    async def get_updates(
            self,
            offset: Optional[int]=None, 
            limit: Optional[int]=None, 
            timeout: Optional[int]=None,
            allowed_updates: Optional[List[str]] = None
        ) -> Optional[dict]:
        data = generate_payload(locals().copy())

        return await self.make_request('getUpdates', data=data)