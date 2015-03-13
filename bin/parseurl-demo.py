#!/usr/bin/python

# quick demo/template for parsing URLs
# extend the "print o" for more complex selection of URLs components
#
# derived from:
# https://docs.python.org/2/library/urlparse.html
# http://stackoverflow.com/questions/1450393/how-do-you-read-from-stdin-in-python

from urlparse import urlparse
import sys

for line in sys.stdin:
    o = urlparse(line)
    print o

