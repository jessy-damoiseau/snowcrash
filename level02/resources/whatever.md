# Level02

---

- On trouve un fichier "level02.pcap" dans le home.
	Les fichiers .pcap sont des fichiers de trames de donnes internet pouvant etre lues avec des outils tels que Wireshark.

- On recupere le fichier sur notre machine avec la commande suivante:
```bash
	scp -P 4242 level02@192.168.56.103:level02.pcap .
```

- On ouvre donc le fichier avec Wireshark et on regarde les trames.

- La trame 43 contient la ligne "Password"

- On ouvre donc le menu contextuel de cette trame et on selectionne "Follow>TCP Stream".

- La fenetre contenant le regroupement des paquets ouverts, on  observe la ligne : 
>	Password; ft_wandr...NDRel.L0L

- En observant la trame en "hex dump" et non en "ASCII", on trouve que les " . " sont en realiter le caractere "7F" qui represente le caractere DEL dans la table ascii.

- En applicant les suppressions de caracteres, on obtient donc:
 >	ft_waNDReL0L

- On fini par se connecter a l'utilisateur flag02 et obtenir le flag.