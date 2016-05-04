#!/usr/bin/python

import sys
from adorocinema import adorocinema

movie = adorocinema.AdoroCinema(' '.join(sys.argv[1:]))
info = movie.getinfo()
for k in info:
    print('%s: %s' % (k,info[k]))
