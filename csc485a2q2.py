import nltk
from nltk import parse_cfg
from nltk.parse import ChartParser, BU_STRATEGY
from nltk.parse import TestGrammar
from nltk import parse

g_s='''
%start S
S -> NP
S -> NP[CASE=nom, ARG=?a] VP[ARG=?a]




NP[NUM=?n, CASE=?c] -> N[NUM=?n, CASE=?c, CAT=PRO]
NP[NUM=pl] -> N[NUM=pl]
NP[NUM=pl] -> N[NUM=pl] PP
NP[NUM=?n] -> Det N[NUM=?n,CAT=N]
NP[NUM=?n] -> Det N[NUM=?n,CAT=N] PP
PP -> P NP[CASE=acc]
VP -> V NP
P -> 'with'
Det -> 'the'
V -> 'fed'
N[NUM=sg, CASE=nom, CAT=PRO] -> 'she'
N[NUM=sg, CASE=acc, CAT=PRO] -> 'him'
N[NUM=sg, CAT=N] -> 'dog'
N[NUM=pl, CAT=N] -> 'puppies'

'''

g=nltk.parse_fcfg(g_s)

parser = parse.FeatureEarleyChartParser(g)
tokens='she fed the dog with puppies with him'.split()
trees = parser.nbest_parse(tokens)

#parser=ChartParser(g,BU_STRATEGY)

for t in trees:
	print t
