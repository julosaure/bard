"""
A module which generates pseudorandom text.

It utilizes Markov chains to produce new text based on
some input text. You could use it, for example, to write a
ten million word science fiction epic using the science
fiction category of the Brown corpus (yes, I have done it).

This module requires NLTK.
"""
import nltk

# Copyright 2010, Zach Denton <z@chdenton.com>
# Licensed under the terms of the GPLv3 or later

# metadata
__author__ = 'Zach Denton'
__author_email__ = 'z@chdenton.com'
__version__ = '0.2'
__url__ = 'http://zacharydenton.com/code/bard/'
__license__ = 'GPLv3'
__longdescr__ = '''
A module for natural language generation. It contains
various natural language generators, which produce new
tokens based on a list of input tokens. It also provides
detokenizers, which attempt to correctly transform a list 
of tokens into formatted text.
'''
__classifiers__ = [
    'Topic :: Text Processing'
]

# packages
import detokenizers; from detokenizers import *
import generators; from generators import *

def generate_text(length=100,corpus=None,generator_type=None):
    tokens = generate(corpus=corpus, length=length, generator_type=generator_type)
    return detokenize(tokens)
