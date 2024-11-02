def validUTF8(data):
    num_cont = 0
    for byte in data:
        if byte < 0 or byte > 255:
            return False
        if num_cont == 0:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                num_cont = 1
            elif byte >> 4 == 0b1110:
                num_cont = 2
            elif byte >> 3 == 0b11110:
                num_cont = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_cont -= 1
    return num_cont == 0

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

a = 5
b = 2
print(a << b)