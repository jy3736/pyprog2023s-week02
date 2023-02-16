# Do not modify this file.  It is used by the autograder.

# Do not modify this file.  It is used by the autograder.

import unittest
from io import StringIO
from unittest.mock import patch
import sys, os

script_name = sys.argv[0]
base_name = os.path.basename(script_name)
lab_name = os.path.splitext(base_name)[0].split("_")[-1]
lab_dir = '../src/' + lab_name

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), lab_dir)))
from main import main

class TestMain(unittest.TestCase):
    
    def test_time_diff(self):
        test_cases = [("1 30 15\n2 0 10\n", "1795\n"), 
                      ("5 15 30\n5 15 31\n", "1\n"),
                      ("10 30 20\n8 15 5\n", "-1\n"),
                      ("0 0 0\n0 0 1\n", "1\n"),
                      ("0 0 0\n1 0 0\n", "3600\n"),
                      ("0 0 0\n23 59 59\n", "86399\n"),
                      ("23 59 59\n0 0 0\n", "-1\n")]
        for test_input, expected_output in test_cases:
            with patch('sys.stdin', StringIO(test_input)):
                with patch('sys.stdout', new=StringIO()) as result:
                    print(f"Testing case:\n{test_input}" )
                    main()
                    self.assertEqual(result.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
