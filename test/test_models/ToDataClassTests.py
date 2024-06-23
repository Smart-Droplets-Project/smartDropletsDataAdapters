import unittest

from ngsildclient import Entity

from sd_data_adapter.models import to_object


class ToDataClassTests(unittest.TestCase):

    def test_good_parameter(self):
        entity = Entity("AgriCrop", "urn:ngsi-ld:AgriCrop:6061c51d-9a9f-428b-900c-759b985868db-id")
        entity.prop("name", "Corn")
        entity.prop("dateCreated", "2024-05-20")
        entity.prop("dateModified", "2024-05-20")
        entity.prop("dataProvider", "BioSense Institute")

        agri_crop = to_object(entity)

        self.assertEqual(agri_crop.id, entity["id"])
        self.assertEqual(agri_crop.type, entity["type"])
        self.assertEqual(agri_crop.name, entity["name"])
        self.assertEqual(agri_crop.dateCreated, entity["dateCreated"])
        self.assertEqual(agri_crop.dateModified, entity["dateModified"])
        self.assertEqual(agri_crop.dataProvider, entity["dataProvider"])

    def test_bad_parameter_type(self):
        with self.assertRaises(TypeError):
            to_object(None)


if __name__ == '__main__':
    unittest.main()