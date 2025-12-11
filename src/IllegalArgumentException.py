class IllegalArgumentException(Exception):
    def __init__(self, msg='numero de assento prioritários maior que assentos total'):
        self.msg = msg
        super().__init__(self.msg)
