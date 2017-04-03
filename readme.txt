DBDM : Closure Algorithm for Functional Dependencies
====================================================

DERUMIGNY Nicolas
KERINEC Emma

Content
=======

readme.txt : this file
results.csv : raw results
plot.png : figure depicting results

/---- closure
 |
 |--- datastruc.py : definition of classes
 |
 |--- libinput.py : treatment of inputs
 |
 |--- clos_algorithms.py : implementation of requested algorithms

The project is available at https://github.com/NicolasDerumigny/DBDM-proj
The option -test has been added to launch automatically unit test.

Open questions
==============

4.1 Justifications of data structures
-------------------------------------
It is object oriented derivated from standard classes, 
so the majority of the functions have not to be implemented again and debuging is faster.


4.2 Strategy for Choose A
-------------------------
We choose A uniformely at random, using random.sample(). 


4.3 Find the bug
-------------------------


6.1 Interestingness of generate
-------------------------------
This set is interesting because each integer n is a key for the set of integers greater than it, 
so it deal with multiple implications and an unique attribute being a key. 


6.2 Setup and methodology
-------------------------
All the results have been taken on the same computer with the following configuration: linux mint 18.2 i5-6600K with 8Go RAM only running on terminal mode.


6.3 Analysis
------------


Additional comments
===================

We are absolutely not sure about the meaning of the BCNF and more generally about the Decompose algorithm.

