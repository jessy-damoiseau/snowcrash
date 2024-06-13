en decompilant le ./level09 on decouvre que celui-ci nous print arg1 avec + index  tout ces charactere
ce qui donne une chaine encrypter

dans token on trouve une chaine encrypter donc on suppose qui faut la decrypter avec la solution inverse

on creer un script python pour ca:

import sys

result = ""

for i, arg in enumerate(sys.argv[1]):
    result += chr(ord(arg)-i)

print(result)

en exectutant la commande:

python /tmp/script.py `cat token`

on obtient le pwd de flag09: f3iji1ju5yuevaus41q1afiuq

puis depuis flag09 on peux faire un getflag