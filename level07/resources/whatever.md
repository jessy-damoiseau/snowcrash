# Level07

---

- En decompilant l'executable, on remarque que le programme lis la variable d'environnement "LOGNAME" puis l'ecris dans un "asprintf" avec un "echo".

- On peut donc modifier la variable d'environement pour faire executer le fichier getflag:
```bash
export LOGNAME='$(getflag)'
```

- Executer l'executable nous donne le flag.