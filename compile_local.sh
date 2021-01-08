#!/usr/bin/env bash
# modify for single question homeworks - change *$question.cpp to *.cpp

while read question; do
  mkdir $question
  find submission -name "*$question.cpp" -exec cp {} $question \;
#  cp $HOMEWORK/submission/*.cpp $HOMEWORK/$question
  g++ $question/*.cpp -o $question/a.out
done < questions.txt

