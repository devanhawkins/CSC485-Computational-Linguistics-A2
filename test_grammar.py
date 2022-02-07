cwd='file:///home/mouse9911/code/days/2009.10.18/csc485/'

o_filename='ParseTrees'

import sys
from nltk import parse_cfg
from nltk.parse import ChartParser, BU_STRATEGY
from nltk.parse import TestGrammar

def read_file(filename):
	handle=open(filename, 'rU')
	ret=''
	for line in handle.readlines():
		if (len(line)>0 and line[0]!='%' and len(line.strip())!=0):
			ret+=line
	handle.close()
	return ret

if __name__=='__main__':
	if len(sys.argv)!=4:
		print '%s grammar lexicon test_sentences' % sys.argv[0]
		sys.exit(1)
	import nltk
	cfg_file=sys.argv[1]
	lex_file=sys.argv[2]
	ts_file=sys.argv[3]
	cfg_string=read_file(cfg_file)
	cfg_string+=read_file(lex_file)
	ts=read_file(ts_file).split('\n')[:-1]
	
	g=parse_cfg(cfg_string)
	parser=ChartParser(g,BU_STRATEGY)
	

	handle=open(o_filename,'w')
	for sentence in ts:
		handle.write(sentence+'\n')
		try:
			results=parser.nbest_parse(sentence.split())
		except ValueError:
			results=[]
		if (len(results)==0):
			print 'FAIL!\t%s' %(sentence)
			handle.write('No parses.'+'\n')
		else:
			print '%d\t%s' % (len(results),sentence)
			for t in results:
				handle.write(str(t)+'\n')
	handle.close()
	
	
