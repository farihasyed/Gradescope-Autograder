#!/usr/bin/env bash
# for local use to create .zip
HOMEWORK=${1?Error: no homework given};
cp -R $HOMEWORK/tests .
cp $HOMEWORK/questions.txt questions.txt
zip -r -X HW$HOMEWORK.zip tests compile.sh customized_json_test_runner.py \
  questions.txt requirements.txt run_autograder run_tests.py \
  setup.sh test_generator.py assignment_specific.py
rm -rf tests
rm questions.txt
