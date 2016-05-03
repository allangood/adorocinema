# Binds to query movie information from Adoro Cinema web site.

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
$ ./search.py deadpool
plot: Ex-militar e mercenário, Wade Wilson (Ryan Reynolds) é diagnosticado com câncer em estado terminal, porém encontra uma possibilidade de cura em uma sinistra experiência científica. Recuperado, com poderes e um incomum senso de humor, ele torna-se Deadpool e busca vingança contra o homem que destruiu sua vida.
rating: 4,8
poster: http://br.web.img3.acsta.net/c_300_300/pictures/16/01/28/19/55/412201.jpg
company: FOX FILMES
title: Deadpool
director: ['Tim Miller']
cast: ['Ryan Reynolds', 'Morena Baccarin', 'Ed Skrein', 'Gina Carano']
genre: [u'A\xe7\xe3o', 'Aventura', u'Com\xe9dia']
```
