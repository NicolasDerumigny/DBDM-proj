from datastruc import *


def parseInput(ioFile, debug):
	''' Parse the input file following the given specification'''
	set_of_func_dep=SetFDs()
	ref_attr={}

	for line in ioFile:
		if len(line.split("->"))==2 and line[0]!="#":
			func_dep_raw=line.split("->")

			precondition=SetAttributes()
			for attr in func_dep_raw[0].split():
				if not(attr in ref_attr):
					ref_attr[attr]=Attribute(attr)
				precondition.add(ref_attr[attr])

			postcondition=SetAttributes()
			for attr in func_dep_raw[1].split():
				if not(attr in ref_attr):
					ref_attr[attr]=Attribute(attr)
				postcondition.add(ref_attr[attr])
			
			set_of_func_dep.add(FD(precondition,postcondition))

	if debug:
		print("Initial set of fun dep:")
		print(set_of_func_dep)

	return set_of_func_dep, ref_attr

def parseAtts(StrAttr, ref_attr, debug):
	''' Parse the Atts string provided to the script'''
	set_of_attr=SetAttributes()
	lst_attr=StrAttr.split()
	for attr in lst_attr:
		if attr not in ref_attr:
			ref_attr[attr]=Attribute(attr)
		set_of_attr.add(ref_attr[attr])
			
	if debug:
		print("Initial set of attributes:", end=" ")
		print(set_of_attr)
	
	return set_of_attr, ref_attr