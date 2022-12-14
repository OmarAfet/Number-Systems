Binarys = []
def Decimal_To_Binary(Decimal):
    if Decimal >= 1:
        Decimal_To_Binary(Decimal // 2)
        Binarys.append(Decimal % 2)

    result = ""
    for i in Binarys:
        result += str(i)

    while len(result) % 4 != 0:
        result = "0" + result
        
    result = " ".join(result[i:i+4] for i in range(0, len(result), 4))
    
    return result

print(Decimal_To_Binary(123))
