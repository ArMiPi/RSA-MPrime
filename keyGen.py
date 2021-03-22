def calc_N(p1, p2, p3):
    return p1 * p2 * p3

def calc_phiN(p1, p2, p3):
    return (p1 - 1) * (p2 - 1) * (p3 - 1)

def get_e():
    return 65537

def calc_d(e, phiN):
    return pow(e, -1, phiN)