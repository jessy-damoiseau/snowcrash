# Level08

---

- Nous avons cette fois ci, deux fichier:
	1. token : dans lequel nous n'avons pas les droits de lecture ou d'ecriture
	2. level08 : un executable

- L'executable, une fois decompile, indique qu'il lis un fichier pris en argument, sauf si son nom contient le mot "token".

- On fait donc un lien symbolique vers le file token et on use ce lien pour l'ouvrir avec l'executable:
```bash
	ln -s $HOME/token /tmp/link && ./level08 /tmp/link
```

- En lancant l'executable, on obtient le flag suivant:
> 	quif5eloekouj29ke0vouxean

- Ce token ne nous permet pas de passer au user suivant du fait que c'est un token et non un flag.
	On peut donc se connecter au user flag08 puis utiliser "getflag".