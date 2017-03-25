import argparse
import sys
import os
import datastruc
import libinput
import clos_algorithms as cl_alg

def main():
	parser = argparse.ArgumentParser(description='Compute the Closure Algorithm for Functionnal Dependencies.')

	group = parser.add_mutually_exclusive_group(required=True)

	group.add_argument('-naive', action='store_const', const="naive",  help='Run naive algorithm')

	group.add_argument('-improved', action='store_const', const="improved",  help='Run improved algorithm')

	group.add_argument('-generate', metavar="n", type=int, help='Generate a set of n FD')

	group.add_argument('-normalized', action='store_const', const="normalized",  help='Normalized an input')

	group.add_argument('-decompose', action='store_const',  const="decomposed", help='Decompose an input')

	group.add_argument('-test', action='store_const',  const="test", help='Decompose an input')

	parser.add_argument('-debug', action='store_const', const="debug",  help='Print Debug')

	parser.add_argument('input', nargs='?', type=str,  help='Input on which reading')

	parser.add_argument('atts', nargs='?', type=str,  help='Algorithm to use')



	#try:
	args = parser.parse_args()


	if args.test!=None:
		# Execute unit tests
		print("Executing Unit tests:")

		tests=[
		("A -> A","A","A"),
		("A -> A","B","B"),
		("A -> A B","A","A B"),
		("A -> B\n B -> C D", "A", "A B C D"),
		("A -> A\n A -> A\n B -> F G","B E","B F G E")
		]
		# Test[i]=( fd, attr, result)
		num=1
		failed=0
		for t in tests:
			print("\n#{}".format(num))
			file=open("/tmp/test",'w')
			file.write(t[0])
			file.close()

			file=open("/tmp/test",'r')
			fun_deps, ref_attr=libinput.parseInput(file, None)
			file.close()

			set_attr, ref_attr=libinput.parseAtts(t[1], ref_attr, None)
			result, ref_attr=libinput.parseAtts(t[2], ref_attr, None)

			print("Naive:")
			closu=cl_alg.naive(set_attr, fun_deps, None)
			if result==closu:
				print("\tPassed")
			else:
				print("\tFailed on input {} with FD {}, output is {} instead of {}".format(t[1], t[0], str(closu), str(result)))
				failed+=1

			print("Improved:")
			print("\tNot implemented yet")
			num+=1
		if failed:
			print("Error: {}/{} tests failed".format(failed, num-1))
		exit()



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
		set_attr, ref_attr=libinput.parseAtts(args.atts, ref_attr, args.debug)

		if args.naive!=None:
			closu=cl_alg.naive(set_attr, fun_deps, args.debug)
			print("The closure of {} is:".format(set_attr))
			print(closu)

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