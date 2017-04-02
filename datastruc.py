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

	def resetAttrLst(self):
		for attr in self:
			attr.lst=SetFDs()


	def union(self, otherSet):
		return SetAttributes(set(self).union(otherSet))

	def difference(self, otherSet):
		return SetAttributes(set(self).difference(otherSet))

	def copy(self):
		return SetAttributes(set(self).copy())

	@staticmethod
	def make(element):
		ret=SetAttributes()
		ret.add(element)
		return ret

	@staticmethod
	def cast(set):
		ret=SetAttributes()
		for elmnt in set:
			ret.add(elmnt)
		return ret

class FD:
	def __init__(self, element1:SetAttributes(), element2:SetAttributes()):
		self.pre=element1
		self.post=element2
		self.count=0

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

	def copy(self):
		return SetFDs(set(self).copy())

	def difference(self, otherSet):
		return SetFDs(set(self).difference(otherSet))

	def union(self, otherSet):
		return SetFDs(set(self).union(otherSet))

	def resetFDCount(self):
		for FD in self:
			FD.count=0

	@staticmethod
	def make(element):
		ret=SetFDs()
		ret.add(element)
		return ret

	@staticmethod
	def cast(set):
		ret=SetFDs()
		for elmnt in set:
			ret.add(elmnt)
		return ret

class FrozenSetAttributes(frozenset):
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

	def difference(self, otherSet):
		return SetAttributes(set(self).difference(otherSet))

	def copy(self):
		return SetAttributes(set(self).copy())


class SetSetAttributes(set):
	def __str__(self):
		str_ret="Set of set:\n"
		for set_attr in self:
			str_ret+=str(set_attr)
			str_ret+="\n"
		return str_ret

	def union(self, otherSet):
		return SetSetAttributes(set(self).union(otherSet))

	def difference(self, otherSet):
		return SetSetAttributes(set(self).difference(otherSet))

	@staticmethod
	def make(init_set):
		ret=SetSetAttributes()
		ret.add(FrozenSetAttributes(init_set))
		return ret