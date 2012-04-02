def partition(xs, pred, transform=lambda x : x) :
	ps,qs = [],[]
	for x in xs :
		if pred(x) :
			ps.append(transform(x))
		else :
			qs.append(transform(x))
	return ps,qs
