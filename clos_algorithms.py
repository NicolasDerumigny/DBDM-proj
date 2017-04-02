import random
from datastruc import *

def naive(set_attr, fun_deps, debug = False):
	'''Compute the closure of ref_attr with respect to fun_dep using the naive algorithm'''
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
	'''Compute the closure of ref_attr with respect to fun_dep using the improved algorithm'''
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

def isAKeyOf(set_attr, fun_deps, debug = False):
	'''Return True if and only if set_attr is a key of schema(fun_deps)'''
	return schema(fun_deps) <= improved(set_attr, fun_deps, debug)

def isInBCNF(set_attr, fun_deps, debug = False):
	'''Return True if and only if fun_deps is in Boyce-Codd Normal Form'''
	for dep in fun_deps:
		if not(dep.post<=dep.pre):
			if not(isAKeyOf(dep.pre, fun_deps, debug)):
				return False
	return True

def decompose(fun_deps, set_attr, debug = False):
	'''Decompose fun_deps into a BCNF'''
	F=reduce(minimize(fun_deps, debug), debug)
	R=SetSetAttributes(set_attr)
	while not(isInBCNF(F, debug)):
		#TODO: find r: r in in R, r not in BCNF, and x in r such that x->y is a nontrivial non-key of F
		R=R.difference(SetSetAttributes(r)).union(SetSetAttributes([improved(dep.pre, F, debug), (r.difference(improved(dep.pre, F, debug)).union(dep.pre))]))
	return R