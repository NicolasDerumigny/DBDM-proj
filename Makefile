MAINFILE=closure

#INPUT=examples/CCF2015P.txt
INPUT=examples/ex.TD3.txt

all: test1


test1: $(MAINFILE).py 
	python3 $^ -naive -debug $(INPUT) ""


clean:
	rm -rf *~ $(PACKAGE)*.py *.pyc  __pycache*
