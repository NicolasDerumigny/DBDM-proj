import random
import itertools
from datastruc import *

def naive(set_attr, fun_deps, debug = False):
	'''Compute the closure of ref_attr with respect to fun_deps using the naive algorithm'''
	done=False
	out=set_attr.copy()
	while (not(done)):
		done=True
		for dep in fun_deps:
			if (dep.pre <= out) and not(dep.post <= out):
				out=out.union(dep.post)
				done=False
	
	return out

def improved(set_attr, fun_deps, debug = False):
	'''Compute the closure of ref_attr with respect to fun_deps using the improved algorithm'''
	for dep in fun_deps:
		dep.setCount()
		for attr in dep.pre:
			attr.addLst(dep)

	closure=set_attr.copy()
	update=set_attr.copy()
	while(len(update) != 0):
		A = random.sample(update,1)
		A = A[0]
		update.remove(A)
		for dep in A.lst:
			dep.decCount()
			if dep.isCountNull():
				update=update.union(dep.post.difference(closure))
				closure=closure.union(dep.post)

	fun_deps.resetFDCount()
	closure.resetAttrLst()
	return closure

def checkIfProve(fun_deps, FD, debug = False):
	'''Return True if and only if fun_deps involves FD'''
	return FD.post <= improved(FD.pre, fun_deps, debug)

def minimize(fun_deps, debug = False):
	'''Return a minimal (in cardinality) cover of fun_deps'''
	G=SetFDs()
	
	for dep in fun_deps:
		G.add(FD(dep.pre,improved(dep.pre, fun_deps)))

	for dep in G:
		if checkIfProve(G.difference(SetFDs.make(dep)),dep):
			G=G.difference(SetFDs.make(dep))
	return G

def reduce(fun_deps, debug = False):
	'''Return a cover of fun_deps with reduced left-hand sides'''
	mini=fun_deps.copy()
	for dep in mini:
		W=dep.post
		for A in dep.post:
			G=mini.difference(SetFDs.make(dep)).union(SetFDs.make(\
				FD(dep.pre,W.difference(SetAttributes.make(A)))))
			if checkIfProve(G, dep):
				W=W.difference(SetAttributes.make(A))

		mini=mini.difference(SetFDs.make(dep)).union(SetFDs.make(\
			FD(dep.pre,W)))

	

	return mini

def schema(fun_deps, debug = False):
	'''Return the set of attributes involved in fun_deps'''
	schem=SetAttributes()
	for dep in fun_deps:
		schem=schem.union(dep.pre).union(dep.post)
	return schem

def isAKeyOf(set_attr, set_attr2, fun_deps:SetFDs(), debug = False):
	'''Return True if and only if set_attr is a key of schema(fun_deps)'''
	return checkIfProve(fun_deps, FD(set_attr, set_attr2))

def isNotInBCNF(set_set_attr, fun_deps, debug = False):
	'''Return True if and only if all fun_deps is in Boyce-Codd Normal Form'''
	for r in set_set_attr:
		for dep in fun_deps:
			if dep.pre <= r and dep.post <= r and not(dep.post<=dep.pre):
				#if dep is not trivial
				if not(isAKeyOf(dep.pre, r, fun_deps, debug)):
					return r, dep
	return None, None

def decompose(fun_deps, set_attr, debug = False):
	'''Decompose fun_deps into a BCNF'''
	F=reduce(minimize(fun_deps, debug), debug)
	R=SetSetAttributes.make(set_attr)
	while True:
		r, dep=isNotInBCNF(R, F, debug)
		if not(r):
			break

		if debug:
			print(R)
			print(dep)
			print("r : {}".format(r))
		R.add(FrozenSetAttributes(improved(dep.pre, F, debug)))
		
		if debug:
			print("adding {} and {}".format(improved(dep.pre, F, debug), r.difference(improved(dep.pre, F, debug)).union(dep.pre)))
		R.add(FrozenSetAttributes(r.difference(improved(dep.pre, F, debug)).union(dep.pre)))
		R=R.difference(SetSetAttributes.make(r))
		if debug:
			print("apres")
			print(R)
	return R.difference(FrozenSetAttributes())