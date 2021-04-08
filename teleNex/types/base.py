from . import Field


class TeleObj:
    _corrects = {}

    def __init__(self, json_data: dict):
        cur_type: TeleObj = type(self)

        for key, value in json_data.items():
            field: Field = cur_type.__dict__.get(key)

            if field is None:
                key = cur_type._corrects.get(key)
                field = cur_type.__dict__.get(key)

            if field is None:
                #raise TypeError(f'{type(self).__name__} got an unexpected keyword argument \'{key}\'')
                continue

            self.__dict__[key] = field.make_obj(value, self)

    
    def dict(self):
        corrects = { field_name: json_name for json_name, field_name in self._corrects.items() }

        res = {}

        for key, value in self.__dict__.items():
            if key in corrects:
                key = corrects[key]

            if type(value) is list:
                res[key] = [ 
                    item.dict() if isinstance(item, TeleObj) 
                    else [obj.dict() if isinstance(obj, TeleObj) else obj for obj in item] if isinstance(item, list)
                    else item
                    
                    for item in value 
                ]
            elif isinstance(value, TeleObj):
                res[key] = value.dict()
            else:
                res[key] = value

        return res