def Add_Binary(a: int, b: int) -> str:
    x = int(str(a), 2)
    y = int(str(b), 2)
    z = bin(x + y)[2:]
    
    while len(z) % 4 != 0:
        z = "0" + z

    return type(" ".join(z[i:i+4] for i in range(0, len(z), 4)))