def Multiply_Octal(a: str, b: str) -> str:
    x = int(a, 8)
    y = int(b, 8)
    z = oct(x * y)[2:]

    return z