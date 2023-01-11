def Hexadecimal_To_Binary(Hexadecimal: str) -> int:
    x = bin(int(Hexadecimal, 16))[2:]

    while len(x) % 4 != 0:
        x = "0" + x

    return " ".join(x[i:i+4] for i in range(0, len(x), 4))

