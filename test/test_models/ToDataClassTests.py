import unittest

from sd_data_adapter.models import to_object


class ToDataClassTests(unittest.TestCase):
    def test_bad_parameter_type(self):
        with self.assertRaises(TypeError):
            to_object(None)


if __name__ == '__main__':
    unittest.main()