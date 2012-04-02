import  survey
import  bPmf

def ProbIn(pmf,min,max) : 
	tot = 0.0
	for t,p in pmf.Items() :
		# print "t:=",t,",p:=",p
		if t >= min and t <= max :
			tot += p 
	return tot

def ProbEarly(pmf) :
	return ProbIn(pmf,0,37)

def ProbOnTime(pmf) :
	return ProbIn(pmf,38,40)

def ProbLate(pmf) :
	return ProbIn(pmf,41,100)

def PmfFor(liveBirths,pred):
	return bPmf.MakePmfFromList([round(p.prglength) for p in liveBirths if pred(p)])


def FindBins(msg,liveBirths,pred) :
	pmf = PmfFor(liveBirths,pred)
	print msg
	print 'ProbEarly():', ProbEarly(pmf)
	print 'ProbOnTime():', ProbOnTime(pmf)
	print 'ProbLate():', ProbLate(pmf)
	print 

table = survey.Pregnancies()
table.ReadRecords()
liveBirths = [x for x in table.records if x.outcome == 1]
FindBins('Total Live Births',liveBirths, lambda p: True)
FindBins('First Births ',liveBirths, lambda p: p.birthord == 1)
FindBins('Other Births ',liveBirths, lambda p: p.birthord != 1)

pmfFirst = PmfFor(liveBirths,lambda p: p.birthord == 1)
pmfOther = PmfFor(liveBirths,lambda p: p.birthord > 1)
print 'Relative Prob. Early:',ProbEarly(pmfFirst)/ProbEarly(pmfOther)
print 'Relative Prob. On Time:',ProbOnTime(pmfFirst)/ProbOnTime(pmfOther)
print 'Relative Prob. Late:',ProbLate(pmfFirst)/ProbLate(pmfOther)


