def Add_Hexadecimal(a: str, b: str) -> str:
    x = int(a, 16)
    y = int(b, 16)
    z = (hex(x + y)[2:]).upper()

    return z