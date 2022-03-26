import unittest

from dataClasses.libs.module2.browserHistory import BrowserHistory

class TestBrowserHistory(unittest.TestCase):
    def setUp(self):
        self.methods = {
            0: "visit",
            1: "visit",
            2: "visit",
            3: "back",
            4: "back",
            5: "forward",
            6: "visit",
            7: "forward",
            8: "back",
            9: "back"
        }
        self.args = {
            0: "\"google.com\"",
            1: "\"facebook.com\"",
            2: "\"youtube.com\"",
            3: 1,
            4: 1,
            5: 1,
            6: "\"linkedin.com\"",
            7: 2,
            8: 2,
            9: 7
        }

        self.exp_outputs = {
            0: None, 
            1: None, 
            2: None, 
            3: "facebook.com", 
            4: "google.com", 
            5: "facebook.com", 
            6: None, 
            7: "linkedin.com", 
            8: "google.com", 
            9: "leetcode.com"
        }

    def test_visit(self):
        testObject = BrowserHistory('leetcode.com')
        output = testObject.visit("google.se")
        exp_output = None

        msg = "Expected: {exp_output}, got: {output}"
        self.assertEqual(output, exp_output, msg.format(exp_output=exp_output, output=output))


    def test_back(self):
        testObject = BrowserHistory('leetcode.com')
        testObject.visit("google.se")
        testObject.visit("facebook.se")
        
        exp_output = "google.se"
        output = testObject.back(1)

        msg = "Expected: {exp_output}, got: {output}"
        self.assertEqual(output, exp_output, msg.format(exp_output=exp_output, output=output))

    def test_back_more_steps_than_data(self):
        testObject = BrowserHistory('leetcode.com')
        testObject.visit("google.se")
        testObject.visit("facebook.se")

        exp_output = "leetcode.com"
        output = testObject.back(10)

        msg = "Expected: {exp_output}, got: {output}"
        self.assertEqual(output, exp_output, msg.format(exp_output=exp_output, output=output))

    def test_forward(self):
        testObject = BrowserHistory('leetcode.com')
        testObject.visit("google.se")
        testObject.visit("facebook.se")
        testObject.back(1)
        
        exp_output = "facebook.se"
        output = testObject.forward(1)

        msg = "Expected: {exp_output}, got: {output}"
        self.assertEqual(output, exp_output, msg.format(exp_output=exp_output, output=output))

    def test_forward_more_steps_than_data(self):
        testObject = BrowserHistory('leetcode.com')
        testObject.visit("google.se")
        testObject.visit("facebook.se")
        testObject.back(1)
        
        exp_output = "facebook.se"
        output = testObject.forward(10)

        msg = "Expected: {exp_output}, got: {output}"
        self.assertEqual(output, exp_output, msg.format(exp_output=exp_output, output=output))

    def test_output(self):
        testSubject = BrowserHistory('leetcode.com')

        exec_cmd = "testSubject.{method}({arg})"
        msg = "Not equal on step {i} out of {j}"

        for i in self.methods.keys():
            output = eval(exec_cmd.format(method=self.methods[i], arg=self.args[i]))
            self.assertEqual(output, self.exp_outputs[i], msg.format(i=i, j=len(self.methods.keys())-1))

        
