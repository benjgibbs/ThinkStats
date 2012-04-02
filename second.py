import thinkstats as ts
import math
import survey 
import bPmf 

def printStats(xs,what) :
	m,v = ts.MeanVar(xs)
	print 'Considering',len(xs),'cases'
	print 'The Mean',what,'is', m
	print 'The Variance in',what,'is', v
	print 'The Std Dev in',what,'is', math.sqrt(v)
	pmf = bPmf.MakePmfFromList(xs)
	print 'PmfMean:', pmf.Mean()
	print 'PmfVar:', pmf.Var()


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

def RemainingLifetime(pmf,age):
	newTot = 0
	for x,y in [ (a,b) for a,b in  pmf.Items() if a>age] :
		newTot += y
	print 'NewTot:',newTot
	result = pmf.Copy()
	
	for x,y in result.Items():
		if x <= age :
			result.Mult(x,0.0)
		else :
			result.Mult(x,1.0/newTot)
	return result
	
pmf = bPmf.MakePmfFromList([1,2,2,3,3,3,4,4,5])
pmf.Print()
print
pmf2 = RemainingLifetime(pmf,3)	
pmf2.Print()

print
print 'pmf.Mean()',pmf.Mean()
print 'pmf.Var()',pmf.Var()
print 'pmf2.Mean()',pmf2.Mean()
print 'pmf2.Var()',pmf2.Var()

