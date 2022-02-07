from nltk import parse_cfg, draw
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
NP_N -> Det N_countable | Det AdjP N_countable | NP_N PP | Det_mass AdjP N_mass | Adj N_mass | Det_mass N_mass | N_mass
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
VP -> AdvP V_NP NP_obj | V_NP AdvP NP_obj | AdvP V_NP AdvP NP_obj | V_NP NP_obj
VP -> AdvP V_NP_PP_to NP_obj PP_to | V_NP_PP_to AdvP NP_obj PP_to | AdvP V_NP_PP_to AdvP NP_obj PP_to | V_NP_PP_to NP_obj PP_to
VP -> AdvP V_NP_PP_from NP_obj PP_from | V_NP_PP_from AdvP NP_obj PP_from | AdvP V_NP_PP_from AdvP NP_obj PP_from | V_NP_PP_from NP_obj PP_from
VP -> AdvP V_NP_VP_to NP_obj VP_to | V_NP_VP_to AdvP NP_obj VP_to | AdvP V_NP_VP_to AdvP NP_obj VP_to | V_NP_VP_to NP_obj VP_to
VP -> AdvP V_S S | V_S AdvP S | AdvP V_S AdvP S | V_S S
VP -> AdvP V_S_that S_that | V_S_that AdvP S_that | AdvP V_S_that AdvP S_that | V_S_that S_that
S_that -> 'that' S
PP_from -> 'from' NP
PP_to -> 'to' NP
VP_to -> 'to' V_bs
NP_obj -> NP | NPro_obj
P -> 'in' | 'with' | 'on' | 'for' | 'to' | 'from' | 'onto' | 'of'
N_countable -> 'cat' | 'eggplant' | 'poodle' | 'autoclave' | 'package' | 'elephant' | 'hovercraft' | 'menu'
N_mass -> 'fur' | 'Fur' | 'Cheese'  | 'cheese' | 'Help' | 'help'
NPrp -> 'Nadia' | 'Ross'
NPro_sub -> 'she' | 'She' | 'he' | 'He' | 'they' | 'They' | 'I'
NPro_obj -> 'her' | 'him' | 'me' 
Det -> 'the' | 'The' | 'a' | 'A' | 'some' | 'Some'
Det_mass -> 'the' | 'The' | 'some' | 'Some' 
Adj -> 'long' | 'soft' | 'tall' | 'handsome'
Adv -> 'immediately' | 'slowly' | 'already' | 'really' | 'always'
V_ps -> 'left' | 'ate' | 'arrived' | 'married' | 'feasted' | 'prevented' | 'jumped' | 'ran' | 'was'
V_pp -> 'left' | 'eaten' | 'arrived' | 'married' | 'feasted' | 'prevented' | 'jumped' | 'run' | 'been' 
V_bs -> 'leave' | 'eat' | 'arrive' | 'marry' | 'feast' | 'prevent' | 'jump' | 'run' | 'be' 
V_ger -> 'leaving' | 'eating' | 'arriving' | 'marrying' | 'feasting' | 'preventing' | 'jumping' | 'running' | 'being'
Aux_modal -> 'can' | 'could' | 'may' | 'might' | 'must' | 'will' | 'would' | 'should' | 'shall'
Aux_perfect -> 'has'
Aux_perfect_bs -> 'have'
Aux_progressive -> 'is'
Aux_progressive_bs -> 'be'
Aux_progressive_pp -> 'been'
Aux_passive -> 'is'
Aux_passive_bs -> 'be'
Aux_passive_pp -> 'been'
V_NP -> 'fondled' | 'brought' | 'told' | 'believed' | 'wanted' | 'reminded'
V_NP_PP_to -> 'brought'
V_NP_PP_from -> 'brought'
V_NP_VP_to -> 'told'
V_S -> 'believed'
V_S_that -> 'believed'
''')


test={}
test['accept'] = [
'Nadia left immediately',
'The cat slowly ate',
'The cat with the long soft fur slowly ate',
'the cat with the long soft fur slowly ate',
'She arrived',
'she arrived',
'Nadia will leave',
'Nadia has left',
'Nadia may have been leaving',
'Nadia will be married',
'Nadia has been feasting',
'Nadia might have been prevented',
'Nadia fondled the eggplant',
'The handsome poodle left',
'The handsome poodle brought Ross',
'The handsome poodle brought Ross to the autoclave',
'Nadia brought a package for the cheese',
'They told her',
'They told her to jump onto the elephant',
'They told her to run from her to him',
'Ross was on the hovercraft',
'Ross was already on the hovercraft',
'Ross already was on the hovercraft',
'She believed Ross',
'She believed Ross was on the hovercraft',
'She believed that Ross was on the hovercraft',
'She really wanted help',
'Cheese was always on the menu',
'The eggplant reminded Nadia',
'The eggplant reminded Nadia of Ross',
'They believed Ross was on the eggplant',
'He believed Ross was on the cheese to the eggplant',
'help was always in the cheese',
'They always wanted really help',
'He told her to run in the cheese'
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
'They have left',
'I have left', #fails because don't support I
'Nadia found',
'Ross brought to him',
'They told to jump onto the elephant',
'that she believed that Ross was on the hovercraft',
'That she believed that Ross was on the hovercraft'
]


parser=ChartParser(grammar,BU_STRATEGY)

#for t in parser.nbest_parse('She believed Ross was on the hovercraft'.split()):
#	print t
#	draw.draw_trees(t)

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

















