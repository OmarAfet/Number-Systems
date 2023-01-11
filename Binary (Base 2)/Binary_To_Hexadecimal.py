def binary_to_hexadecimal(binary: str) -> str:
    return (hex(int(binary, 2))[2:]).upper()