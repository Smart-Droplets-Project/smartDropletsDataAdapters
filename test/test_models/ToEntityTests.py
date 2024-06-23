import unittest

from sd_data_adapter.models import to_ngsi_ld
from sd_data_adapter.models.agri_food import AgriCrop


class ToEntityTests(unittest.TestCase):

    def test_bad_parameter_type(self):
        with self.assertRaises(TypeError):
            to_ngsi_ld(None)

    def test_good_parameter(self):
        agri_crop = AgriCrop(
            id="urn:ngsi-ld:AgriCrop:6061c51d-9a9f-428b-900c-759b985868db-id",
            type="AgriCrop",
            name="Corn",
            dateCreated="2024-05-20",
            dateModified="2024-05-20",
            dataProvider="BioSense Institute"
        )

        entity = to_ngsi_ld(agri_crop)

        self.assertEqual(entity["id"], agri_crop.id)
        self.assertEqual(entity["type"], agri_crop.type)
        self.assertEqual(entity["name"]["value"], agri_crop.name)
        self.assertEqual(entity["dateCreated"]["value"], agri_crop.dateCreated)
        self.assertEqual(entity["dateModified"]["value"], agri_crop.dateModified)
        self.assertEqual(entity["dataProvider"]["value"], agri_crop.dataProvider)


if __name__ == '__main__':
    unittest.main()