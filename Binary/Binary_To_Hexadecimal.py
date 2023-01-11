def binary_to_hexadecimal(binary: str) -> int:
    return (hex(int(binary, 2))[2:]).upper()