
# Level13

---

- On trouve dans le home un fichier executable.

- En le recuperant et decompilant, on observe une chaine de charactere en dur qui  passe dans une fonction "ft_des" qui la dechiffre.

- On copie le flag encrypter en local pour obtenir le flag decrypte.

```c
#include <stdio.h>
#include <string.h>

char * ft_des(char *str_encrypted)

{
    char cVar1;
    char *pcVar2;
    unsigned int uVar3;
    char *pcVar4;
    short bVar5;
    unsigned int local_20;
    int local_1c;
    int local_18;
    int local_14;
    
    bVar5 = 0;
    pcVar2 = strdup(str_encrypted);
    local_1c = 0;
    local_20 = 0;
    do {
        uVar3 = 0xffffffff;
        pcVar4 = pcVar2;
        do {
            if (uVar3 == 0) break;
            uVar3 = uVar3 - 1;
            cVar1 = *pcVar4;
            pcVar4 = pcVar4 + (unsigned int)bVar5 * -2 + 1;
        } while (cVar1 != '\0');
        if (~uVar3 - 1 <= local_20)
        {
            return pcVar2;
        }
        if (local_1c == 6)
        {
            local_1c = 0;
        }
        if ((local_20 & 1) == 0)
        {
            if ((local_20 & 1) == 0)
            {
                for (local_14 = 0; local_14 < "0123456"[local_1c]; local_14 = local_14 + 1) {
                    pcVar2[local_20] = pcVar2[local_20] + -1;
                    if (pcVar2[local_20] == '\x1f')
                    {
                        pcVar2[local_20] = '~';
                    }
                }
            }
        }
        else
        {
            for (local_18 = 0; local_18 < "0123456"[local_1c]; local_18 = local_18 + 1) {
                pcVar2[local_20] = pcVar2[local_20] + '\x01';
                if (pcVar2[local_20] == '\x7f')
                {
                    pcVar2[local_20] = ' ';
                }
            }
        }
        local_20 = local_20 + 1;
        local_1c = local_1c + 1;
    } while( 1 );
}

int main()
{
	printf("%s", ft_des("boe]!ai0FB@.:|L6l@A?>qJ}I"));
	return 0;
}
```