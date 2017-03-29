class FD:
	def __init__(self, element1, element2): 
		'''element1 and element2 are two SetAttributes'''
		self.pre=element1
		self.post=element2
		self.count=None

	def __str__(self):
		return"{} -> {}\n".format(self.pre, self.post)

	def setCount(self):
		self.count=len(self.pre)

	def decCount(self):
		self.count-=1

	def isCountNull(self):
		return self.count==0
			
	
class SetFDs(set):
	def __str__(self):
		str_ret=""
		for FD in self:
			str_ret+=str(FD)
		return str_ret


class Attribute() :
	def __init__(self, name):
		self.id=name
		self.lst=SetFDs()

	def __str__(self):
		return self.id

	def addLst(self, FD):
		self.lst.add(FD)

class SetAttributes(set):
	def __str__(self):
		str_ret="{"
		for i in range(len(list(self))):
			str_ret+=str(list(self)[i])
			if i!=len(list(self))-1:
				str_ret+=", "
		str_ret+="}"
		return str_ret

	def union(self, otherSet):
		return SetAttributes(set(self).union(otherSet))


class SetSetAttributes(set):
	def __init__(self, init_set):
		self=set(frozenset(init_set))

	def __str__(self):
		str_ret=""
		for attr in self:
			str_ret+="Set: {"
			str_ret+=str(attr)
			str_ret+="}\n"
		return str_ret