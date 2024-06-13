Level06

---

- On as un fichier cette fois-ci ecris en PHP.

- Ce fichier indique que le programme attend un argument et du fait qu'il passe dans la fonction:
		file_get_contents()
	On peut y ecrire ce que l'on souhaite executer

- La ligne qui y seras lue passeras dans un regex et seras modifier a cause de la ligne :
```php
	$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
```

- Le regex, fonctionne ainsi ceci:
```
	/(\[x (.*)\])/e
```
 \   () : indique un groupe de capture
\	\\\[x : indique que la ligne commence avec le groupe de characteres "\[x"
\  .* : le . indique "n'importe que caracteres" et le * indique que le precedent test (ici . ) est repeter autant de fois qu'il est vrai.
\ \\] : montre que la ligne fini par ]
\ /e : Indique que la ligne une fois lue sera interpreter tel une commande

- Avec toutes ces informations, on peut creer un fichier contenant la ligne suivante:
```bash
[x {${exec(getflag)}}]
```

- Une fois l'executable lancer avec ce fichier en argument, on peut recuperer le flag.