def Binary_To_Decimal(Bin):
    # Here's how it works 0*(2**7) + 1*(2**6) + 1*(2**5) 1*(2**4) + 1*(2**3) + 0*(2**2) 1*(2**1) + 1*(2**0)
    return int(Bin, 2)

# Example "01111011" (Binary) to "123" (Decimal)
print(Binary_To_Decimal("01111011"))
