import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)
print 'Number of live births', reduce(
	lambda a,b : a + int(b.outcome == 1), table.records, 0 )

def check (f, rs) :
	count = 1 
	totalLength = 0.0
	longest = 0
	for r in rs :
		if f(r) :
			count += 1
			totalLength += r.prglength
			if r.prglength > longest :
				longest = r.prglength
	return count, totalLength/count, longest


a, b, c = check(lambda x : x.birthord == 1 and x.outcome == 1, table.records)
print 'Number of first births', a
print 'Average length', b
print 'Longest', c

d, e, f = check(lambda x : x.birthord > 1 and x.outcome == 1, table.records)
print 'Number of non-first births', d
print 'Average length', e
print 'Longest', f

print 'Difference', abs(b-e) * 7 * 24, 'hours'
