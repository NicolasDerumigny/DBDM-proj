MAINFILE=closure

#INPUT=examples/CCF2015P.txt
INPUT=examples/ex.TD3.txtz
ATTR="A E C"
all: test1

test-all: test1

test1: $(MAINFILE).py 
	python3 $^ -naive -debug $(INPUT) $(ATTR)


clean:
	rm -rf *~ $(PACKAGE)*.py *.pyc  __pycache*
