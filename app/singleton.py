class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.val = 0

    def set(self, new_value):
        self.val = new_value

    def get(self):
        return self.val
