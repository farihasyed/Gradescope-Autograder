#!/usr/bin/env bash
# modify for single question homeworks - change *$question.cpp to *.cpp

while read question; do
  mkdir /autograder/source/$question
  find /autograder/submission/ -name "*$question.cpp" -exec cp {} /autograder/source/$question \;
  g++ /autograder/source/$question/*.cpp -o /autograder/source/$question/a.out
done < /autograder/source/questions.txt

