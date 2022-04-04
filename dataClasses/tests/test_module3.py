import unittest
import string

from dataClasses.libs.module3.ceasarCipher import build_coder, build_encoder, build_decoder, apply_coder, apply_shift

class TestBuildCoder(unittest.TestCase):
    def setUp(self):
        self.test_object = build_coder(3)
        self.expected_output = {
            ' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J', 
            'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O', 
            'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', 
            'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd', 
            'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 
            'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 
            'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 
            'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'
        } 
        self.test_shift_range = range(-27, 27)
        self.list_of_char = ' ' + string.ascii_lowercase
    
    def test_input_type(self):
        self.assertRaises(TypeError, build_coder, 1.0)
        self.assertRaises(TypeError, build_coder, '1')
        self.assertRaises(TypeError, build_coder, 'a')
        self.assertRaises(TypeError, build_coder, ['a'])
        self.assertRaises(TypeError, build_coder, ('a'))

    def test_output_type(self):
        msg = "Output not of type {type}"
        self.assertEqual(type(self.test_object), dict, msg.format(type=dict))

    def test_output(self):
        msg = "Input: {chr}, Expected: {a}, Got: {b}"
        for chr in self.expected_output.keys():
            self.assertEqual(
                self.test_object[chr], 
                self.expected_output[chr], 
                msg.format(chr=chr, a = self.expected_output[chr], b=self.test_object[chr])
            )

    def test_shift_range(self):
        msg = "Input: {chr}, shift: {shift} - Expected: {a}, Got: {b}"
        for shift in self.test_shift_range:
            coder = build_coder(shift)
            index = self.list_of_char.index('a') + shift
            if index >= len(self.list_of_char):
                index -= len(self.list_of_char)

            self.assertEqual(
                coder['a'], 
                self.list_of_char[index], 
                msg.format(chr='a', shift=shift, a=coder['a'], b=self.list_of_char[index])
            )
    def test_shift_out_of_range(self):
        test_range = range(-1000, 1000)
        for shift in test_range:
            if shift not in self.test_shift_range:
                self.assertRaises(ValueError, build_coder, shift)
            else:
                pass

class TestApplyCoder(unittest.TestCase):
    def setUp(self):
        self.decoded_string = "Hello, world!"
        self.encoded_string = "Khoor,czruog!"

    def test_encoder(self):
        output = apply_coder(self.decoded_string, build_encoder(3))
        self.assertEqual(output, self.encoded_string)

    def test_decoder(self):
        output = apply_coder(self.encoded_string, build_decoder(3))
        self.assertEqual(output, self.decoded_string)
    
class TestApplyShift(unittest.TestCase):
    def setUp(self):
        self.decoded_string = "This is a test."
        self.encoded_string = "Apq hq hiham a."

        self.encoder_shift = 8
        self.decoder_shift = -8

    def test_input(self):
        self.assertRaises(TypeError, apply_shift, None, 1)
        self.assertRaises(TypeError, apply_shift, 1, 1)
        self.assertRaises(TypeError, apply_shift, ['This is a test.'], 1)
 
        self.assertRaises(TypeError, apply_shift, self.decoded_string, None)
        self.assertRaises(TypeError, apply_shift, self.decoded_string, 1.0)
        self.assertRaises(TypeError, apply_shift, self.decoded_string, '1')
        self.assertRaises(TypeError, apply_shift, self.decoded_string, [1])

    def test_encoder(self):
        output = apply_shift(self.decoded_string, self.encoder_shift)
        self.assertEqual(output, self.encoded_string)

    def test_decoder(self):
        output = apply_shift(self.encoded_string, self.decoder_shift)
        self.assertEqual(output, self.decoded_string)