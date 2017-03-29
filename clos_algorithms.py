import random

def naive(set_attr, fun_deps, debug = False):
	'''Compute the closure of ref_attr with respect to fun_dep using the naive algorithm'''
	done=False

	while (not(done)):
		done=True
		for dep in fun_deps:
			if (dep.pre <= set_attr) and not(dep.post <= set_attr):
				set_attr=set_attr.union(dep.post)
				done=False
	
	return set_attr

def improved(set_attr, fun_deps, debug = False):
	'''Compute the closure of ref_attr with respect to fun_dep using the improved algorithm'''
	for dep in fun_deps:
		dep.setCount()
		for attr in dep.pre:
			attr.addLst(dep)

	closure=set_attr
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
	return closure

def checkIfProve(fun_deps, FD, debug = False):
	'''Return True if and only if fun_deps involves FD'''
	closFD=improved(FD.post, fun_deps, debug)
	return FD.pre <= closFD

def minimize(fun_deps, debug = False):
	'''Return a minimal (in cardinality) cover of fun_deps'''
	G=SetFDs()
	
	for dep in fun_deps:
		G=G.union(FD(dep.pre,improved(dep.pre, fun_deps)))

	for dep in G:
		if checkIfProve(G.difference(setFDs(dep)),dep):
			G=G.difference(setFDs(dep))

	return G

def reduce(fun_deps, debug = False):
	'''Return a cover of fun_deps with reduced left-hand sides'''
	mini=fun_deps.copy()
	for dep in mini:
		W=dep.post
		for A in dep.post:
			G=Mini.difference(setFDs(dep)).union(SetFD(FD(dep.pre,W.difference(A))))
			if checkIfProve(G, dep):
				W=W.difference(SetAttributes(A))
		mini=mini.difference(SetFDs(dep)).union(SetFD(FD(dep.pre,W)))
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