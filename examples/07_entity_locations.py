

from sd_data_adapter.models.agri_food import AgriParcel
from sd_data_adapter.api import upload

from geojson import Point, Polygon, MultiLineString, FeatureCollection

if __name__ == '__main__':

    rows = MultiLineString([
            [
                [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
            ],
            [
                [105.0, 1.0], [106.0, 2.0], [107.0, 3.0], [108.0, 4.0]
            ]
        ])

    point = Point([102.0, 0.5])

    polygon = Polygon([[(2.38, 57.322), (-120.43, 19.15), (23.194, -20.28), (2.38, 57.322)]])

    parcel = AgriParcel(
        alternateName="ParcelWithFeatureCollections",
        description="A parcel which has a collection of features",
        location=FeatureCollection([
            point, rows, polygon
        ])
    )

    print(parcel)

    print(upload(parcel))