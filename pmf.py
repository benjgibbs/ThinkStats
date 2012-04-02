
def MakeHistFromList(xs):
	return Hist(xs)

def MakeHistFromDic(dic):
	h = Hist()
	h.histDic = dic
	return h

def MakePmfFromList(xs):
	return Pmf(Hist(xs))

def MakePmfFromDic(xs):
	return Pmf(MakeHistFromDic(xs))

class Pmf:
	def __init__(self,hist):
		self.SetHist(hist)
		self.Initialize()
	
	def SetHist(self,hist):
		self.hist=hist	

	def Initialize(self):
		pmf =  {}
		n = float(len(self.hist.Items()))
		for x,freq in self.hist.Items():
			pmf[x] = freq/n
		self.pmfDic = pmf
	
	def Prob(self,n):
		return self.pmfDic.get(n,0)
	
	def Items(self):
		return self.pmfDic.items()

	def Render(self):
		return self.pmfDic.keys(),self.pmfDic.values()
	
	def Mult(self,n,x):
		self.pmfDic[n] = self.Prob(n) * x
	
	def Inc(self,n,x):
		self.pmfDic[n] = self.Prob(n) + x
	
	def Total(self):
		total = 0
		for x in self.pmfDic.values():
			total += x
		return total
	
	def Renormalize(self):	
		total = self.Total()
		for k,v in self.pmfDic.items():
			self.pmfDic[k] = v/total
	
	def Copy(self):
		copy = Pmf(Hist([]))
		copy.pmfDic = self.pmfDic.copy()
		return copy
	
	def Print(self):
		for a,b in self.Items():
			print a,':',b

	def Mean(self): 
		result = 0.0
		for x,p in self.Items(): 
			result += x * p
		return result
	
	def Var(self): 
		mu = self.Mean()
		result = 0.0
		for x,p in self.Items():
			result += (p * ((x - mu) ** 2.0))
		return result

class Hist:
	def __init__(self,xs=[]):
		hist =  {}
		for x in xs:
			hist[x] = hist.get(x,0) + 1
		self.histDic = hist

	def Freq(self,n): 
		return self.histDic.get(n,0)
	
	def Values(self):
		return self.histDic.keys()
	
	def Items(self):
		return self.histDic.items()
	
	def Count(self):
		return len(self.Items())

	def Mode(self):
		mk = None
		for k,f in self.Items():
			if mk is None or f > self.Freq(mk):
				mk = k
		return mk
	
	def AllModes(self):
		return sorted(self.Items(), 
			lambda a, b: b[1] - a[1] )

def main():
	h = MakeHistFromList([1,2,2,3,5])
	print 'Freq(2):', h.Freq(2)
	print 'Freq(4):', h.Freq(4)
	print 'Values():', h.Values()
	print 'Values()/Freq()'
	for val in sorted(h.Values()):
		print val, h.Freq(val)
	print 'Items()'
	for val,freq in h.Items():
		print val, freq
	print 'Mode()',h.Mode()
	print 'AllModes()',h.AllModes()
	print 
	pmf = MakePmfFromList([1,2,2,3,5])
	print 'Prob(2):',pmf.Prob(2)
 	pmf.Inc(2,0.2)	
	print 'Inc(2,0.2):',pmf.Prob(2)
 	pmf.Mult(2,0.5)
	print 'Total:', pmf.Total()
	pmf2 = pmf.Copy()
	print 'Renormalizing'
	pmf.Renormalize()
	print 'Total:', pmf.Total()
	print 'Pmf2 Total: ',pmf2.Total()

if __name__ == '__main__':
	main()
