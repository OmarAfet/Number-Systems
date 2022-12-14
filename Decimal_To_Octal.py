Octals = []
def Decimal_To_Octal(Dec):
    if Dec >= 1:
        Decimal_To_Octal(int(Dec / 8))
        Octals.append(Dec % 8)
    
    result = ""
    for i in Octals:
        result += str(i)
    
    return result

print(Decimal_To_Octal(468))
