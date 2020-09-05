#!/usr/bin/env bash
# modify for single question homeworks - change *$question.cpp to *.cpp

while read question; do
  find $HOMEWORK/submission -name "*$question.cpp" -exec cp {} $HOMEWORK/$question \;
  cp $HOMEWORK/submission/*.cpp $HOMEWORK/$question
  g++ $HOMEWORK/$question/*.cpp -o $HOMEWORK/$question/a.out
done < $HOMEWORK/questions.txt

