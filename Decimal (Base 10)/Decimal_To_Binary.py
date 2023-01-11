def Decimal_To_Binary(decimal: int) -> str:
    x = bin(decimal)[2:]

    while len(x) % 4 != 0:
        x = "0" + x

    return x