class API:
    def __new__(cls, *args, **kwargs):
        print('вызов __new__' + str(cls))
        return super().__new__(cls)

    def __init__(self, a, b):
        print('вызов __init__' + str(self))
        self.a = a
        self.b = b


pt = API(1, 2)
print(pt)
