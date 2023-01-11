def Subtract_Hexadecimal(a: str, b: str) -> str:
    x = int(a, 16)
    y = int(b, 16)
    if y > x:
        z = "-" + (hex(y - x)[2:]).upper()
    else:
        z = (hex(x - y)[2:]).upper()
    
    return z