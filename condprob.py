import survey
import bPmf
import utils 
import matplotlib.pyplot as plot

def condProb(cond, pmf) :
	result = pmf.Copy()
	for i,j in pmf.Items() :
		if i < cond :
			result.Mult(i,0)
	result.Renormalize()
	return result.Prob(cond)

table = survey.Pregnancies()
table.ReadRecords()
liveBirths = [x for x in table.records if x.outcome == 1]
pmf = bPmf.MakePmfFromList([p.prglength for p in liveBirths])

print 'Probability of being born at 39 weeks: ',pmf.Prob(39)
print 'Conditional Probability of being born at 39 weeks if at week 38: ',condProb(39,pmf)


firstBirths,otherBirths = utils.partition(liveBirths, 
	lambda p : p.outcome == 1 and p.birthord == 1, 
	lambda p : p.prglength)

pmf = bPmf.MakePmfFromList(firstBirths)
xs,ys = pmf.Render()
plot.bar(xs, ys, width=0.4, color='white')
pmf = bPmf.MakePmfFromList(otherBirths)
xs,ys = pmf.Render()
plot.bar([x + 0.5 for x in xs], ys, width=0.4, color='blue')

#plot.bar(valsN,probsN, width=0.4, color='blue')
plot.show()
