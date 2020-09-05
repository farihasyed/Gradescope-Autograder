from collections import Counter
HOMEWORK = 7 # modify to reflect current assignment


def hw6_q3(test, output, expected_output, no_space_output, no_space_expected_output):
    student_parity = output.split('\n')[2].rstrip(' ').lstrip(' ').split(' ')
    expected_parity = expected_output.split('\n')[2].rstrip(' ').lstrip(' ').split(' ')
    return Counter(student_parity) == Counter(expected_parity)


def hw7_q2(test, output, expected_output, no_space_output, no_space_expected_output):
    if int(test) == 1:
        phrases = ['true', 'areanagrams']
    elif int(test) == 2 or int(test) == 3:
        phrases = ['false', 'arenotanagrams']
    for phrase in phrases:
        if no_space_output.lower().find(phrase) != -1:
            result = True
            break
        else:
            result = False
    return result


def hw7_q6(test, output, expected_output, no_space_output, no_space_expected_output):
    if int(test) == 1:
        expected = ['5', '2', '6']
    elif int(test) == 2:
        expected = ['9', '2', '6', '7', '8']
    for element in expected:
        if no_space_output.lower().find(element) != -1:
            result = True
        else:
            result = False
            break
    return result


def hw10(test, output, expected_output, no_space_output, no_space_expected_output):
    return no_space_output.find(no_space_expected_output) != -1


APPLICABLE = applicable = {6: {3: hw6_q3}, 7: {2: hw7_q2, 6: hw7_q6}, 10: {1: hw10}}