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
		print(set_of_func_dep)

	return set_of_func_dep, ref_attr

def parseAtts(StrAttr, debug, set_fd):
	''' Parse the Atts string provided to the script'''
	pass