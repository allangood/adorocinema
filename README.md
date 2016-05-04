## Binds to query movie information from Adoro Cinema web site.

### This is a very simple class to get informations from Adoro Cinema web site.

### Example:
```python
#!/usr/bin/python

import sys
from adorocinema import adorocinema

movie = adorocinema.AdoroCinema(' '.join(sys.argv[1:]))
info = movie.getinfo()
for k in info:
    print('%s: %s' % (k,info[k]))
```

```
$ ./movieinfo.py titanic
plot: Jack Dawson (Leonardo DiCaprio) é um jovem aventureiro que, na mesa de jogo, ganha uma passagem para a primeira viagem do transatlântico Titanic. Trata- se de um luxuoso e imponente navio, anunciado na época como inafundável, que parte para os Estados Unidos. Nele está também Rose DeWitt Bukater (Kate Winslet) , a jovem noiva de Caledon Hockley (Billy Zane). Rose está descontente com sua vida, já que sente-se sufocada pelos costumes da elite e não ama Caledon. Entre tanto, ela precisa se casar com ele para manter o bom nome da família, que está falida. Um dia, desesperada, Rose ameaça se atirar do Titanic, mas Jack conseg ue demovê-la da ideia. Pelo ato ele é convidado a jantar na primeira classe, onde começa a se tornar mais próximo de Rose. Logo eles se apaixonam, despertando  a fúria de Caledon. A situação fica ainda mais complicada quando o Titanic se choca com um iceberg, provocando algo que ninguém imaginava ser possível: o nau frágio do navio.
rating: 4,6
poster: http://br.web.img2.acsta.net/c_300_300/medias/nmedia/18/89/56/94/20055685.jpg
company: FOX FILMES
title: Titanic
director: ['James Cameron']
cast: ['Leonardo DiCaprio', 'Kate Winslet', 'Billy Zane', 'Kathy Bates']
year: 1997
genre: ['Drama', 'Romance']
```
