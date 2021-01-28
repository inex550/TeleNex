class Field:
    def __init__(self, cls=None, *, parent=None):
        self.cls = cls
        self.parent = parent

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, cls): pass