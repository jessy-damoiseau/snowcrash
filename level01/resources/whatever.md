# Level01

---

- Encore une fois, aucun fichier dans le home.


- En ouvrant le fichier /etc/passwd, on trouve la ligne suivante :
> 	flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash


- On observe le hash pour l'utilisateur flag01:
>	42hDRfypTqqnw


- En utilisant l'outil "John the ripper", on obtient le mot de passe suivant:
> 	abcdefg


- De nouveau, on se connecte a l'utilisateur flag01 puis on lance la commande ``` getflag ```