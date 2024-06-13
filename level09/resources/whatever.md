# Level09

---

- Nous avons cette fois-ci un fichier token lisible et un executable.

- Le fichier token contient une chaine cryptee et l'executable qui une fois decompile, indique:
	- prend une chaine de caracteres en argument.
	- Fait une rotation des characteres en fonction de son index.

- Le token etant encrypte et ayant acces a l'algorithme, on peut donc decrypte avec un script python suivant:
```py
import sys

result = ""

for i, arg in enumerate(sys.argv[1]):
    result += chr(ord(arg)-i)

print(result)
```

ou encore:
```py
from __future__ import print_function

import sys


if __name__ == "__main__":
	for index, c in enumerate(list(sys.argv[1])):
		print(chr(ord(c) - index), end='')
	print()
```


- Puis, on execute la commande:
```bash
	python /tmp/script.py `cat token`
```

- On obtient le mot de passe de flag09:
> f3iji1ju5yuevaus41q1afiuq

- Puis, depuis flag09 on peux faire un getflag