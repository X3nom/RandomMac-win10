import random,os

# generate mac adress
adress = 'A4E31B' # nokia OUI is currently used, can be changed
for i in range(3):
    num = random.randint(0,225)
    hex_num = hex(num).lstrip('0x').upper()
    while len(hex_num) < 2:
        hex_num = '0'+hex_num
    adress += hex_num
print(adress)

# Work In Progress