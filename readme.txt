DBDM : Closure Algorithm for Functional Dependencies
====================================================

DERUMIGNY Nicolas
KERINEC Emma

Content
=======

readme.txt  : this file
results.csv : raw results
plot.png    : figure depicting results
result.ods  : open document containing data

/---- closure
 |
 |--- datastruc.py : definition of classes
 |
 |--- libinput.py : treatment of inputs
 |
 |--- clos_algorithms.py : implementation of requested algorithms

The project is available at https://github.com/NicolasDerumigny/DBDM-proj
The option -test has been added to launch automatically unit test, defined in 
file closure.


Open questions
==============

4.1 Justifications of data structures
-------------------------------------
All data structures are class, which inherits from standard pyhton set, 
so the majority of the functions have not to be implemented again. 
Morover, debuging is faster as we can know clearly what is the type of each 
object.


4.2 Strategy for Choose A
-------------------------
We choose A uniformely at random, using random.sample(), as we did not see
a better solution.


4.3 Find the bug
-------------------------
If there is W -> Z, with W = emptyset, then Z should be inside the closure of X,
but as list(emptyset) is not checked, it will not be put inside. Even if it would
be checked, it would still not be inside the coluser as its count would be -1 at the test line 11.


6.1 Interestingness of generate
-------------------------------
This set is interesting because each integer n is a key for the set of integers greater than it, 
so it deal with multiple implications and an unique attribute being a key. Normalized has to
compute the closure (all the elements) and then re-split to get again the former FDs. Besides, 
is it already in normalized form, so it is quite easy to check.


6.2 Setup and methodology
-------------------------
All the results have been taken on the same computer with the following configuration: 
Linux Mint 18.2 (console mode only), on an i5-6600K with 8Go of RAM.


6.3 Analysis
------------
The file plot.png outputs the results. Both algorithms seems quadratic, but the improved one is has an X² cofficient 2.4 times better.



Additional comments
===================

We are absolutely not sure about the meaning of the BCNF and more generally about the Decompose algorithm.

