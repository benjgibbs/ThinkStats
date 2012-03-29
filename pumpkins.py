import thinkstats as ts
import math
import survey 

def printStats(xs,what) :
	m,v = ts.MeanVar(xs)
	print 'Considering',len(xs),'cases'
	print 'The Mean',what,'is', m
	print 'The Variance in',what,'is', v
	print 'The Std Dev in',what,'is', math.sqrt(v)


pumpkinWeights = [1,1,1,3,3,591]
printStats(pumpkinWeights, 'Pumpkin Weight')
print ''
table = survey.Pregnancies()
table.ReadRecords()
printStats(
	[x.prglength for x in table.records if x.birthord == 1 and x.outcome == 1], 
	'Gestation Length of first birth') 

print ''
printStats(
	[x.prglength for x in table.records if x.birthord > 1 and x.outcome == 1], 
	'Gestation Length of not-first birth') 
