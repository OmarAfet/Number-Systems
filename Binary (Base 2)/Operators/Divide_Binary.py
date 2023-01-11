def Divide_Binary(a: str, b: str) -> str:
    x = int(a, 2)
    y = int(b, 2)
    z = bin(x // y)[2:]

    return z