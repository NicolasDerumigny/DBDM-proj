import argparse
import sys
import os
import datastruc
import libinput

def main():
	parser = argparse.ArgumentParser(description='Compute the Closure Algorithm for Functionnal Dependencies.')

	group = parser.add_mutually_exclusive_group(required=True)

	group.add_argument('-naive', action='store_const', const="naive",  help='Run naive algorithm')

	group.add_argument('-improved', action='store_const', const="improved",  help='Run improved algorithm')

	group.add_argument('-generate', metavar="n", type=int, help='Generate a set of n FD')

	group.add_argument('-normalized', action='store_const', const="normalized",  help='Normalized an input')

	group.add_argument('-decompose', action='store_const',  const="decomposed", help='Decompose an input')

	parser.add_argument('-debug', action='store_const', const="debug",  help='Print Debug')

	parser.add_argument('input', nargs='?', type=str,  help='Input on which reading')

	parser.add_argument('atts', nargs='?', type=str,  help='Algorithm to use')



	#try:
	args = parser.parse_args()

	if args.generate!=None:
		# Generate here
		exit()



	if args.input=="-":
		input_source=sys.stdin
	else:
		try:
			input_source=open(args.input,'r')
		except FileNotFoundError:
			print("Error: File {} not found".format(args.input))
			exit(-1)

	fun_deps, ref_attr=libinput.parseInput(input_source, args.debug)

	if args.input!="-":
		input_source.close()


	if args.debug:
		print("Used_attr:")
		print(ref_attr)

	if args.naive!=None or args.improved!=None:
		libinput.parseAtts(args.atts, ref_attr, args.debug)

		if args.naive!=None:
			# Naive version here
			pass

		elif args.improved!=None:
			# Improved version here
			pass

	elif args.normalized!=None:
		# Normalized here
		pass

	elif args.decompose!=None:
		# Decomposed here
		pass

	#except Exception as err:
	#	exc_type, exc_obj, exc_tb = sys.exc_info()
	#	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	#	if debug:
	#		print("{} l.{}: {}" .format(fname, exc_tb.tb_lineno, err))
	#	else:
	#		print(err)




if __name__=='__main__':
	main()