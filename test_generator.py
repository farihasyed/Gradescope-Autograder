import unittest
import os
import os.path
import subprocess
from subprocess import Popen
from gradescope_utils.autograder_utils.decorators import weight
import yaml
import re
from customized_json_test_runner import SEPARATOR
from assignment_specific import HOMEWORK


BASE_DIR = os.environ['BASE_DIR']
EXECUTABLE = 'a.out'


class TestMetaclass(type):
    def __new__(cls, name, bases, attrs):
        data_dir = attrs['data_dir']
        attrs[cls.test_name(data_dir)] = cls.generate_test(data_dir)
        return super(TestMetaclass, cls).__new__(cls, name, bases, attrs)

    @classmethod
    def generate_test(cls, dir_name):
        def load_test_file(path):
            full_path = os.path.join(BASE_DIR, dir_name, path)
            if os.path.isfile(full_path):
                with open(full_path) as f:
                    return f.read()
            return None

        def load_settings():
            settings_yml = load_test_file('settings.yml')

            if settings_yml is not None:
                return yaml.safe_load(settings_yml) or {}
            else:
                return {}

        settings = load_settings()
        question_test = dir_name.split('/')
        question = question_test[0]
        test = question_test[1]

        @weight(settings.get('weight', 0))
        def fn(self):
            from assignment_specific import APPLICABLE
            command = os.path.join(question, EXECUTABLE)
            process = Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
            stdin = load_test_file('input')
            output, errors = process.communicate(stdin)
            expected_output = load_test_file('output')
            msg = settings.get('msg', "Output did not match expected")
            no_space_output = re.sub(r'\s+', '', output)
            no_space_expected_output = re.sub(r'\s+', '', expected_output)
            print(SEPARATOR.join([stdin, expected_output, output]))
            if HOMEWORK in APPLICABLE and int(question) in APPLICABLE[HOMEWORK]:
                result = APPLICABLE[HOMEWORK][int(question)](test, output, expected_output, no_space_output, no_space_expected_output)
                self.assertTrue(result, msg=msg)
            else:
                self.assertEqual(no_space_output, no_space_expected_output, msg=msg)
        fn.__doc__ = 'Question {}, Test {}'.format(question, test)
        return fn

    @staticmethod
    def klass_name(dir_name):
        return 'Question {0}'.format(''.join([x.capitalize() for x in dir_name.split('_')]))

    @staticmethod
    def test_name(dir_name):
        return 'Test {0}'.format(dir_name)


def build_test_class(data_dir):
    klass = TestMetaclass(
        TestMetaclass.klass_name(data_dir),
        (unittest.TestCase,),
        {
            'data_dir': data_dir
        }
    )
    return klass


def find_data_directories():
    tests = {}
    questions = [question for question in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, question))]
    questions.sort()
    for question in questions:
        tests[question] = [input for input in os.listdir(os.path.join(BASE_DIR, question)) if os.path.isdir(os.path.join(BASE_DIR, question, input))]
    return tests
