# CRC-12, CRC-16 and CRC-CCITT

def crc(data, poly):
    bits = list(map(int, data + "0" * (len(poly) - 1)))
    divisor = list(map(int, poly))

    for i in range(len(data)):
        if bits[i] == 1:
            for j in range(len(divisor)):
                bits[i + j] ^= divisor[j]

    return "".join(map(str, bits[-(len(poly) - 1):]))


data = input("Enter binary data: ")

polynomials = {
    "CRC-12": "1100000001111",
    "CRC-16": "11000000000000101",
    "CRC-CCITT": "10001000000100001"
}

for name, poly in polynomials.items():
    print(name, "CRC:", crc(data, poly))

'''
SAMPLE INPUT:
Enter binary data: 1101011011
SAMPLE OUTPUT:
CRC-12 CRC: 110001100100
CRC-16 CRC: 1000101111011001
CRC-CCITT CRC: 1011111011001101
'''