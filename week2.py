def crc(data, poly):
    bits = list(map(int, data + "0" * (len(poly) - 1)))
    divisor = list(map(int, poly))

    for i in range(len(data)):
        if bits[i] == 1:
            for j in range(len(divisor)):
                bits[i + j] ^= divisor[j]

    return "".join(map(str, bits[-(len(poly) - 1):]))


text = input("Enter text: ")

data = ""
for c in text:
    data += format(ord(c), '08b')
print("Binary data:", data)

polynomials = {
    "CRC-12": "1100000001111",
    "CRC-16": "11000000000000101",
    "CRC-CCITT": "10001000000100001"
}

for name, poly in polynomials.items():
    print(name, "CRC:", crc(data, poly))
'''
SAMPLE INPUT:
Enter text: HI
SAMPLE OUTPUT:
Binary data: 0100100001001001
CRC-12 CRC: 101111101101
CRC-16 CRC: 1011000110110000
CRC-CCITT CRC: 0101110110001000
''' 
