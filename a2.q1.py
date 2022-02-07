from nltk import parse_cfg
from nltk.parse import ChartParser, BU_STRATEGY
from nltk.parse import TestGrammar

import sys

#question 1.1 all verbs are intransitive, 
# do not need objects
#NPrp - Proper noun
#NPro - Pro noun
#Adj - Adjective
#Adv - Adverb
#NPPrp - Noun
#NP_Prp -> AdjP NPrp | NPrp ?
grammar=parse_cfg('''
S -> NP VP
PP -> P NP | P NPro_obj
AdvP -> Adv | AdvP Adv
AdjP -> Adj | AdjP Adj
VP -> V AdvP | AdvP V | V | VP PP
NP -> NP_Pro | NP_Prp | NP_N
NP_Pro -> NPro_obj N | NPro_obj AdjP N | NPro_sub
NP_Prp -> AdjP NPrp | NPrp
NP_N -> Det N | Det AdjP N | NP_N PP
N -> 'fur' | 'cat'
NPrp -> 'Nadia' 
NPro_sub -> 'she' | 'She'
NPro_obj -> 'her' | 'Her'
Det -> 'the' | 'The'
Adj -> 'long' | 'soft' | 'tall'
Adv -> 'immediately' | 'slowly'
V -> 'left' | 'ate' | 'arrived'
P -> 'in' | 'with' | 'on'
''')

test={}
test['should accept and does'] = [
'Nadia left immediately',
'The cat with the long soft fur slowly ate',
'the cat with the long soft fur slowly ate',
'She arrived',
'she arrived',
]

test['shouldn\' accept and doesn\'t'] = [
'nadia left immediately',
'Nadia with the long soft fur slowly ate',
'The cat with the tall her arrived',
'The cat with the slowly tall her arrived',
'She with the long soft fur slowly ate',
'The cats with the long soft fur slowly ate', #dont support plural
]


parser=ChartParser(grammar,BU_STRATEGY)

for key in test.keys():
	print key
	for sentence in test[key]:
		try:
			results=parser.nbest_parse(sentence.split())
		except ValueError:
			results=[]
		print '\t%s\t%d' % (sentence,len(results))


















