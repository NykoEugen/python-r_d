import unittest
from unittest import mock

from HW26.task_1 import request_web


class TestRequestWebFunction(unittest.TestCase):

    def test_request_web(self):
        with mock.patch('builtins.print') as mock_print:
            request_web()
            mock_print.assert_called()


if __name__ == '__main__':
    unittest.main()
