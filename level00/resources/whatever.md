
# Level00

---

- On observe aucun fichier dans le home du user actuel, donc on recherche un si un fichier anormal est present.


- On trouve un ficher texte nomme "jhon" sur le chemin /usr/bin/john


- En l'ouvrant avec la commande "cat", on obtient le texte suivant :
> 	cdiiddwpgswtgt


- On peut ensuite decrypter ce code avec les outils suivants:
	- [DCode](https://www.dcode.fr/identification-chiffrement)
	- [CyberChef](https://gchq.github.io/CyberChef/)

- En applicant une rotation de  11 caracteres, on obtient le code suivant :
> 	nottoohardhere


- On se connecte a l'utilisateur flag00:
	```bash
		su flag00
	```


- Pour finir, on lance la commande ```getflag``` pour obtenir le flag:
>	x24ti5gi3x0ol2eh4esiuxias