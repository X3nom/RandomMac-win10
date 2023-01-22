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

# write new mac to registry
os.system('reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\0011" /v NetworkAddress /d '+adress+' /f >null')