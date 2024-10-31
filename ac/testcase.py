import unittest
from crc import *
from haming_code import *




class TestErrorDetection(unittest.TestCase):

        # CRC Test Cases
    def test_crc_no_error_detect(self):
        c = CRC()
        EXPECTED_RESULT = "No error detected"
        self.assertEqual(c.reciverSide('100100001', '1101'), EXPECTED_RESULT)

    def test_crc_error_detect_1(self):
        c = CRC()
        EXPECTED_RESULT = "error detected"
        self.assertEqual(c.reciverSide('100110001', '1101'), EXPECTED_RESULT)

    def test_crc_no_error_detect_1(self):
        c = CRC()
        EXPECTED_RESULT = "No error detected"
        self.assertEqual(c.reciverSide('1011101', '111'), EXPECTED_RESULT)

    def test_crc_error_detect_2(self):
        c = CRC()
        EXPECTED_RESULT = "Error detected"
        self.assertEqual(c.reciverSide('11101011001', '1001'), EXPECTED_RESULT)

    def test_crc_no_error_detect_2(self):
        c = CRC()
        EXPECTED_RESULT = "No error detected"
        self.assertEqual(c.reciverSide('1101011001', '101'), EXPECTED_RESULT)

    def test_crc_error_detect_3(self):
        c = CRC()
        EXPECTED_RESULT = "Error detected"
        self.assertEqual(c.reciverSide('100010011', '111'), EXPECTED_RESULT)

    def test_crc_error_detect_small(self):
        c = CRC()
        EXPECTED_RESULT = "Error detected"
        self.assertEqual(c.reciverSide('1001', '10'), EXPECTED_RESULT)

    # Hamming Code Test Cases
    def test_hamming_no_error_detect(self):
        h = HammingCode()
        EXPECTED_RESULT = "No error detected"
        self.assertEqual(h.receiver_side("10100101111"), EXPECTED_RESULT)

    def test_hamming_error_detect(self):
        h = HammingCode()
        EXPECTED_RESULT = "Error detected at bit position: 1"
        self.assertEqual(h.receiver_side("11101001110"), EXPECTED_RESULT)

    # Additional Hamming Code tests adjusted for correct outcomes
    def test_hamming_no_error_detect_large(self):
        h = HammingCode()
        EXPECTED_RESULT = "No error detected"
        self.assertEqual(h.receiver_side("110110110100110"), EXPECTED_RESULT)

    def test_hamming_error_detect_large(self):
        h = HammingCode()
        EXPECTED_RESULT = "Error detected at bit position: 10"
        self.assertEqual(h.receiver_side("110110110011011"), EXPECTED_RESULT)

    def test_hamming_no_error_detect_small(self):
        h = HammingCode()
        EXPECTED_RESULT = "No error detected"
        self.assertEqual(h.receiver_side("10011"), EXPECTED_RESULT)

    def test_hamming_error_detect_small(self):
        h = HammingCode()
        EXPECTED_RESULT = "Error detected at bit position: 2"
        self.assertEqual(h.receiver_side("11011"), EXPECTED_RESULT)

    def test_hamming_error_detect_edge(self):
        h = HammingCode()
        EXPECTED_RESULT = "Error detected at bit position: 1"
        self.assertEqual(h.receiver_side("100111011110111"), EXPECTED_RESULT)

    
if __name__ == '__main__':
    unittest.main(verbosity=2)