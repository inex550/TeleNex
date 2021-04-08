class Field:
    def __init__(self, cls=None, *, parent=None, two_dim=False):
        self.cls = cls
        self.parent = parent
        self.two_dim = two_dim

    def __get__(self, instance, cls): pass

    def make_obj(self, value, instance):
        if self.parent is list:
            if self.two_dim:
                return [ [self.cls(obj) for obj in item_list] for item_list in value ]
            else:
                return [self.cls(obj) for obj in value] if self.cls else value

        elif self.cls is ...:
            return type(instance)(value)

        elif self.cls is not None:
            return self.cls(value)

        else:
            return value