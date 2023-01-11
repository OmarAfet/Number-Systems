def Subtract_Octal(a: str, b: str) -> str:
    x = int(a, 8)
    y = int(b, 8)
    if y > x:
        z = "-" + oct(y - x)[2:]
    else:
        z = oct(x - y)[2:]
    
    return z