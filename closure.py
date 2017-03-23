import argparse
import datastruc


def main():
	parser = argparse.ArgumentParser(description='Compute the Closure Algorithm for Functionnal Dependencies.')


	group = parser.add_mutually_exclusive_group(required=True)

	group.add_argument('-naive', action='store_const', const="naive",  help='Run naive algorithm')

	group.add_argument('-improved', action='store_const', const="improved",  help='Run improved algorithm')

	group.add_argument('-generate', metavar="n", help='Generate a set of n FD')

	group.add_argument('-normalized', action='store_const', const="normalized",  help='Normalized an input')

	group.add_argument('-decompose', action='store_const',  const="decomposed", help='Decompose an input')


	parser.add_argument('input', nargs='?', type=str,  help='Input on which reading')

	parser.add_argument('atts', nargs='?', type=str,  help='Algorithm to use')



	try:
		args = parser.parse_args()
		print(args)

		if args.naive!=None:
			exit()

		if args.improved!=None:
			exit()

		if args.generate!=None:
			exit()

		if args.normalized!=None:
			exit()

		if args.decompose!=None:
			exit()


	except Exception as err:
		print(err)





if __name__ == '__main__':
    main()