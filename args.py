class Args:
    def __init__(self, arguments):
        self.np = int(arguments[1])             # Quantidade de primos utilizados
        self.min_pot = int(arguments[2])        # Limitante inferior para geração dos primos (10**min_pot)
        self.max_pot = int(arguments[3])        # Limitante superior para geração dos primos (10**max_pot)
        self.msg = " ".join(arguments[4:])      # Mensagem que será utilizada