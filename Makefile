MAINFILE=closure

#INPUT=examples/CCF2015P.txt
INPUT=examples/ex.TD3.txt
ATTR="A E C"
all: $(MAINFILE).py 
	python3 $^ -naive -debug $(INPUT) $(ATTR)

test: $(MAINFILE).py 
	python3 $^ -test



clean:
	rm -rf *~ $(PACKAGE)*.py *.pyc  __pycache*
