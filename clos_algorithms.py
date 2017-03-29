import random

def naive(set_attr, fun_deps, debug):
	'''Compute the closure of ref_attr with respect to fun_dep using the naive algorithm'''
	done=False

	while (not(done)):
		done=True
		for dep in fun_deps:
			if (dep.pre <= set_attr) and not(dep.post <= set_attr):
				set_attr=set_attr.union(dep.post)
				done=False
	
	return set_attr

def improved(set_attr, fun_deps, debug):
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