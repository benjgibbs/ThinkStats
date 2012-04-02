import  survey
import  bPmf
import matplotlib.pyplot as plot


table = survey.Pregnancies()
table.ReadRecords()
liveBirths = [x for x in table.records if x.outcome == 1]
firstBirthLength = [x.prglength for x in liveBirths if x.birthord == 1]
otherBirthLength = [x.prglength + 0.5 for x in liveBirths if x.birthord > 1]
firstPmf = bPmf.MakePmfFromList(firstBirthLength)
otherPmf = bPmf.MakePmfFromList(otherBirthLength)

args1 = {'color': 'blue' }
args2 = {'color': 'red' }
vals1,probs1 = firstPmf.Render()
valsN,probsN = otherPmf.Render()
plot.bar(vals1,probs1, width=0.4, color='white')
plot.bar(valsN,probsN, width=0.4, color='blue')
plot.show()

