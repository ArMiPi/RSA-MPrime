class Args:
    def __init__(self, arguments):
        self.np = int(arguments[1])
        self.min_pot = int(arguments[2])
        self.max_pot = int(arguments[3])
        self.msg = " ".join(arguments[4:])