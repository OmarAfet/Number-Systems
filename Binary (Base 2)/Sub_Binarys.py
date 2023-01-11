def Sub_Binary(a: str, b: str) -> str:
    x = int(a, 2)
    y = int(b, 2)
    if y > x:
        z = "-" + bin(y - x)[2:]
    else:
        z = bin(x - y)[2:]
    
    return z