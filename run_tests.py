import unittest
from customized_json_test_runner import CustomizedJSONTestRunner
from test_generator import find_data_directories, build_test_class, TestMetaclass
import os

RESULTS_PATH = os.environ['RESULTS_PATH']

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = find_data_directories()
    for question in tests.keys():
        for test in tests[question]:
            name = os.path.join(str(question), str(test))
            klass = build_test_class(name)
            suite.addTest(klass(TestMetaclass.test_name(name)))
    with open(RESULTS_PATH, 'w') as f:
        runner = CustomizedJSONTestRunner(stdout_visibility='hidden', visibility='hidden', stream=f)
        runner.run(suite)


