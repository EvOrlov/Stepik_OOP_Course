class Vector:
    def __init__(self, **kwargs):
        self.values = dict(kwargs)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if item in self.values.keys():
            return self.values[item]
        else:
            raise IndexError("key not found")

    def __setitem__(self, key, value):
        if key in self.values.keys():
            self.values[key]=value
        else:
            raise IndexError("key not found")

    def __delitem__(self, key):
        if key in self.values.keys():
            del self.values[key]
        else:
            raise IndexError("key not found")