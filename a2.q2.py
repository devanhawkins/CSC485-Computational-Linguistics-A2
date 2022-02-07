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
#Do not need to repeat the Aux_progressive_x and Aux_passive_x  def
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
V -> Aux_modal modal | Aux_perfect perfect | Aux_progressive progressive | Aux_passive passive | V_ps
modal -> perfect_bs | progressive_bs | passive_bs | V_bs
perfect_bs -> Aux_perfect_bs perfect
progressive_bs -> Aux_progressive_bs progressive
passive_bs -> Aux_passive_bs passive
perfect -> progressive_pp | passive_pp | V_pp
progressive_pp -> Aux_progressive_pp progressive
passive_pp -> Aux_passive_pp passive
progressive -> passive_ger | V_ger
passive_ger -> Aux_passive_ger passive
passive -> V_pp
P -> 'in' | 'with' | 'on'
N -> 'fur' | 'cat'
NPrp -> 'Nadia'
NPro_sub -> 'she' | 'She'
NPro_obj -> 'her' | 'Her'
Det -> 'the' | 'The'
Adj -> 'long' | 'soft' | 'tall'
Adv -> 'immediately' | 'slowly'
V_ps -> 'left' | 'ate' | 'arrived' | 'married' | 'feasted' | 'prevented' 
V_pp -> 'left' | 'eaten' | 'arrived' | 'married' | 'feasted' | 'prevented'
V_bs -> 'leave' | 'eat' | 'arrive' | 'marry' | 'feast' | 'prevent'
V_ger -> 'leaving' | 'eating' | 'arriving' | 'marrying' | 'feasting' | 'preventing'
Aux_modal -> 'can' | 'could' | 'may' | 'might' | 'must' | 'will' | 'would' | 'should' | 'shall'
Aux_perfect -> 'has'
Aux_perfect_bs -> 'have'
Aux_progressive -> 'is'
Aux_progressive_bs -> 'be'
Aux_progressive_pp -> 'been'
Aux_passive -> 'is'
Aux_passive_bs -> 'be'
Aux_passive_pp -> 'been'
''')

test={}
test['accept'] = [
'Nadia left immediately',
'The cat with the long soft fur slowly ate',
'the cat with the long soft fur slowly ate',
'She arrived',
'she arrived',
'Nadia will leave',
'Nadia has left',
'Nadia may have been leaving',
'Nadia will be married',
'Nadia has been feasting',
'Nadia might have been prevented'
]

test['reject'] = [
'nadia left immediately',
'Nadia with the long soft fur slowly ate',
'The cat with the tall her arrived',
'The cat with the slowly tall her arrived',
'She with the long soft fur slowly ate',
'The cats with the long soft fur slowly ate', #dont support plural
'Nadia will left',
'Nadia has could leave',
'Nadia has had left',
'They have left', #dont support they
'I have left', #dont support I
]


parser=ChartParser(grammar,BU_STRATEGY)

#for t in parser.nbest_parse('Nadia may have been leaving'.split()):
#	print t

print 'Should Accept'
for sentence in test['accept']:
	results=parser.nbest_parse(sentence.split())
	if len(results)==0:
		print 'FAIL!!'
		sys.exit()
	else:
		print '\t%s\t%d' % (sentence,len(results))


print 'Should Fail'
for sentence in test['reject']:
	try:
		results=parser.nbest_parse(sentence.split())
	except ValueError:
		results=[]
	if len(results)!=0:
		print 'FAIL!!'
		sys.exit()
	else:
		print '\t%s\t%d' % (sentence,len(results))

















