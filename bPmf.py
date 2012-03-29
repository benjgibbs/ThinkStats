
def MakeHistFromList(xs) :
	return Hist(xs)

class Hist :
	def __init__(self,xs):
		hist =  {}
		for x in xs :
			hist[x] = hist.get(x,0) + 1
		
		pmf =  {}
		n = float(len(xs))
		for x,freq in hist.items() :
			pmf[x] = freq/n
		self.histDic = hist
		self.pmfDic = pmf

	def Freq(self,n): 
		return self.histDic.get(n,0)
	
	def Values(self):
		return self.histDic.keys()
	
	def Items(self):
		return self.histDic.items()

	def Mode(self):
		mk = None
		for k,f in self.Items() :
			if mk is None or f > self.Freq(mk) :
				mk = k
		return mk
	
	
	def AllModes(self) :
		return sorted(self.Items(), 
			lambda a, b : b[1] - a[1] )



def main() :
	h = MakeHistFromList([1,2,2,3,5])
	print "Freq(2):", h.Freq(2)
	print "Freq(4):", h.Freq(4)
	print "Values():", h.Values()
	print "Values()/Freq()"
	for val in sorted(h.Values()):
		print val, h.Freq(val)
	print "Items()"
	for val,freq in h.Items():
		print val, freq
	print "Mode()",h.Mode()
	print "AllModes()",h.AllModes()

if __name__ == '__main__':
	main()
