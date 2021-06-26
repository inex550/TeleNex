from . import Field, TeleObj


class LoginUrl(TeleObj):
    url: str = Field()
    forward_text: str = Field()
    bot_username: str = Field()
    request_write_access: str = Field()