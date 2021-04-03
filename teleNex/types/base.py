from . import Field


class TeleObj:
    _corrects = {}

    def __init__(self, json_data: dict):
        cur_type: TeleObj = type(self)

        for key, value in json_data.items():
            field: Field = cur_type.__dict__.get(key)

            if field is None:
                fname = cur_type._corrects.get(key)
                field = cur_type.__dict__.get(fname)

            if field is None:
                raise TypeError(f'{type(self).__name__} got an unexpected keyword argument \'{key}\'')

            self._make_field(key, value, field)

    def _make_field(self, key: str, value, field: Field):
        if value is None:
            self.__dict__[key] = None
            return

        if field.parent is list:
            objs = [field.cls(obj) for obj in value] if field.cls else value
            self.__dict__[key] = objs
        elif field.cls and issubclass(field.cls, TeleObj):
            self.__dict__[key] = field.cls(value)
        elif field.cls is ...:
            self.__dict__[key] = type(self)(value)
        else:
            self.__dict__[key] = value