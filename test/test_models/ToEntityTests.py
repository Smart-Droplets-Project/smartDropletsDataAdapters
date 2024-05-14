import unittest

from sd_data_adapter.models import to_ngsi_ld


class ToEntityTests(unittest.TestCase):

    def test_bad_parameter_type(self):
        with self.assertRaises(TypeError):
            to_ngsi_ld(None)


if __name__ == '__main__':
    unittest.main()