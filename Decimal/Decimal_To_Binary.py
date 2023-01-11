def Decimal_To_Binary(decimal: int) -> int:
    x = bin(decimal)[2:]

    while len(x) % 4 != 0:
        x = "0" + x

    return " ".join(x[i:i+4] for i in range(0, len(x), 4))