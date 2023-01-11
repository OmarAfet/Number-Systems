def Hexadecimal_To_Binary(Hexadecimal: str) -> str:
    x = bin(int(Hexadecimal, 16))[2:]

    while len(x) % 4 != 0:
        x = "0" + x

    return x