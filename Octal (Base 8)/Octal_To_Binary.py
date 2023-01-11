def Octal_To_Binary(Octal: int) -> int:
    x = bin(int(str(Octal), 8))[2:]

    while len(x) % 4 != 0:
        x = "0" + x

    return x