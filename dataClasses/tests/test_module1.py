import unittest

from dataClasses.libs.module1.caseConvert import convert_case

class TestConvert(unittest.TestCase):
    def setUp(self):
        self.string_to_test = "Hello, World."
        self.cases = ["camel", "snake", "kebab", 'pascal', "uppercasesnake"]
        self.outputs = ["helloWorld", "hello_world", "hello-world", "HelloWorld", "HELLO_WORLD"]

        self.long_string_to_test = "Hello, World, This, String, Is, Longer."
        self.long_outputs = [
            "helloWorldThisStringIsLonger",
            "hello_world_this_string_is_longer",
            "hello-world-this-string-is-longer",
            "HelloWorldThisStringIsLonger",
            "HELLO_WORLD_THIS_STRING_IS_LONGER"
            ]

    def test_raise_TypeError(self):
        self.assertRaises(TypeError, convert_case, None)

    def test_raise_ValueError(self):
        self.assertRaises(ValueError, convert_case, 'Hello, World.', 'camels')

    def test_output(self):
        msg = "{case}: {output_from_function}, {output}"

        for i in range(len(self.cases)):
            output = convert_case(self.string_to_test, self.cases[i])
            self.assertEqual(output, self.outputs[i], msg.format(case=self.cases[i], output_from_function=output, output=self.outputs[i]))

    def test_output_with_long_string(self):
        msg = "{case}: {output_from_function}, {output}"

        for i in range(len(self.cases)):
            output = convert_case(self.long_string_to_test, self.cases[i])
            self.assertEqual(output, self.long_outputs[i], msg.format(case=self.cases[i], output_from_function=output, output=self.long_outputs[i]))
