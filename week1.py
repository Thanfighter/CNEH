def character_count(data):
    return str(len(data) + 1) + data


def character_stuffing(data):
    data = data.replace("ESC", "ESCESC")
    data = data.replace("FLAG", "ESCFLAG")
    return "FLAG " + data + " FLAG"


def bit_stuffing(bits):
    result = ""
    count = 0

    for bit in bits:
        result += bit

        if bit == "1":
            count += 1
            if count == 5:
                result += "0"
                count = 0
        else:
            count = 0

    return "01111110" + result + "01111110"


data = input("Enter character data: ")
bits = input("Enter binary data: ")

print("Character Count:", character_count(data))
print("Character Stuffing:", character_stuffing(data))
print("Bit Stuffing:", bit_stuffing(bits))

'''
SAMPLE INPUT:
Enter character data: AFLAGB
Enter binary data: 0111110111111
SAMPLE OUTPUT:
Character Count: 7AFLAGB
Character Stuffing: FLAG AESCFLAGB FLAG
Bit Stuffing: 0111111001111100111110101111110
'''
