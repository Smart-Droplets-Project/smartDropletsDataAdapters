import unittest

from sd_data_adapter.models.smartDataModel import SmartDataModel
from sd_data_adapter.models.agrifood import AgriFarm

class ModelTests(unittest.TestCase):

    def test_minimal_object_setup(self):
        '''
        An instance of any SmartDataModel needs to have
        an ID and Type.
        '''

        a = AgriFarm()

        self.assertEqual(AgriFarm.__name__, a.type)
        self.assertIsNotNone(a.id)

    def test_id_not_overwritten(self):

        id_val = "new_id"

        a = AgriFarm(id=id_val)

        self.assertEqual(a.id, id_val)
