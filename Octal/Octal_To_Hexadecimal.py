def Octal_To_Hexadecimal(Octal: int) -> str:
    return (hex(int(str(Octal), 8))[2:]).upper()