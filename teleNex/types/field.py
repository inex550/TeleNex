class Field:
    def __init__(self, cls=None, *, parent=None):
        self.cls = cls
        self.parent = parent

    def __get__(self, instance, cls): pass