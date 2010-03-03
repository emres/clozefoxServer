import cgi
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import mail

from nltk import pos_tag, word_tokenize
from nltk.stem.porter import *


import sys
sys.path.append('./nlplib')
from NLPlib import *

class NLTKTest(webapp.RequestHandler):
    def get(self):
        # tokenList = word_tokenize("John's big idea isn't all that bad.")
        
        # tokenList = pos_tag(word_tokenize("John's big idea isn't all that bad.")) 

        stemmer = PorterStemmer()
        plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
                   'died', 'agreed', 'owned', 'humbled', 'sized',
                   'meeting', 'stating', 'siezing', 'itemization',
                   'sensational', 'traditional', 'reference', 'colonizer',
                   'plotted']
        singles = []
        for plural in plurals:
            singles.append(stemmer.stem(plural))


        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('Hello test!')
        self.response.out.write(singles)


        nlProcessor = NLPlib()

        s = "Very little is known about Beethoven's childhood. He was baptized  on December 17, 1770 and was probably born a few days before that. [1][4][5][6]  Beethoven's parents were Johann van Beethoven (1740 in Bonn - December 18, 1792) and Maria Magdalena Keverich (1744 in Ehrenbreitstein - July 17, 1787)."

        v = nlProcessor.tokenize(s)
        t = nlProcessor.tag(v)
        for i in range(len(v)):
            self.response.out.write(v[i] + "(" + t[i] + ")<br/>")
