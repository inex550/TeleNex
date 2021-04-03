from typing import Any, Optional


class Response:
    ok: bool = None
    result: Optional[Any] = None
    error_code: Optional[int] = None
    description: Optional[str] = None


    def __init__(self, json_data: dict):
        for k, v in json_data.items():
            self.__dict__[k] = v

    def result_instance(self, cls):
        if type(self.result) is list:
            result = [cls(obj) for obj in self.result]
        else:
            result = cls(self.result)

        return result