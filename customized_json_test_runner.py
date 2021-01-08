from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner, JSONTestResult

SEPARATOR = '#~'


class CustomizedJSONTestResult(JSONTestResult):
    def buildResult(self, test, err=None):
        passed = (err == None)
        weight = 0.0
        tags = self.getTags(test)
        number = self.getNumber(test)
        visibility = self.getVisibility(test)
        score = 0.0

        output = self.getOutput().split(SEPARATOR)
        result = {
            "name": self.getDescription(test),
            "score": score,
            "max_score": weight if passed else 1,
            "result": "Passed" if passed else "Failed"
        }
        if tags:
            result["tags"] = tags
        if output and len(output) > 2:
            result['input'] = output[0]
            result['outputs'] = {}
            result['outputs']['expected'] = output[1]
            result['outputs']['student'] = output[2]
        if visibility:
            result["visibility"] = visibility
        if number:
            result["number"] = number
        return result


class CustomizedJSONTestRunner(JSONTestRunner):
    resultclass = CustomizedJSONTestResult
