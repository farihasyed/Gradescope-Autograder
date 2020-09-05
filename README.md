# Gradescope-Autograder
Autograder for use with Gradescope to automatically compile, run, test, and grade C++ student assignments for 
NYU Bridge to Tandon.

Adapted from this Gradescope example: [Diff General](https://github.com/gradescope/autograder_samples/tree/master/diff_general)

###For each assignment:
* Change `HOMEWORK` in [assignment_specific](assignment_specific.py) to reflect current assignment
* Update [questions.txt](questions.txt) with questions in assignment
* [tests](tests) with input and outputs for each question in [questions.txt](questions.txt)

###Execute
####Gradescope
```
/autograder/run_autograder
```
####Local
```
./run_autograder_local 7
```

The main difference between the two scripts is that I have separate directories for each assignment locally, and the test cases 
reside within the assignment's test directory. In addition, the environment variables`BASE_DIR` and `RESULTS_PATH`
have different values on Gradescpe vs locally.

###Tests
Actual test cases not included in this repository. Within the [tests](tests) directory, each question has its own directory. 
Within each question's directory, each test case has its own directory. Finally, within each test case directory are the
files input and output. Input is fed into the student's program, and output is the expected output. Below is a 
representation of the directory structure. I used integers to represent each question and its test cases e.g. 
tests/2/3 represents question 2, test case 3. 

````
Gradescope-Autograder
|   compile.sh
|   run_tests.py
│   ... 
└───tests
│   │
│   └───QUESTION NUMBER
│   |   |
│   |   └───TEST CASE NUMBER   
│   |   |   | input
│   |   |   | output
|   |   |    
│   |   └───TEST CASE NUMBER   
│   |   |   | input
│   |   |   | output
|   |   |  
│   |   └───...
|   |
│   └───...   
````

[Gradescope autograder documentation](https://gradescope-autograders.readthedocs.io/en/latest/)
