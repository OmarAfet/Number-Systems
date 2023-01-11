def Octal_To_Hexadecimal(Octal: int) -> int:
    return (hex(int(str(Octal), 8))[2:]).upper()