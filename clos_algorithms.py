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