def Sum_Binarys(Bin1, Bin2):
    max_len = max(len(Bin1), len(Bin2))
    Bin1 = Bin1.zfill(max_len)
    Bin2 = Bin2.zfill(max_len)

    result = ''
    carry = 0
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if Bin1[i] == '1' else 0
        r += 1 if Bin2[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        carry = 0 if r < 2 else 1

    if carry != 0:
        result = '1' + result

    return result.zfill(max_len)

print(Sum_Binarys("00110010", "00110111"))
