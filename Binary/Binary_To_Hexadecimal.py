def binary_to_hexadecimal(binary: int) -> str:
    return (hex(int(str(binary), 2))[2:]).upper()