

from sd_data_adapter.models.autonomous_mobile_robot import CommandMessage
from sd_data_adapter.api import upload, is_alive_check

from sd_data_adapter.client import DAClient

from geojson import Point, Polygon, MultiLineString, FeatureCollection

if __name__ == '__main__':
    HOST: str = "34.89.222.243"
    PORT: int = 1026
    DAClient.get_instance(HOST, PORT)

    print("Connection is alive:", is_alive_check())

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

    parcel = CommandMessage(
        command="run:RunSpraying",
        waypoints=FeatureCollection([
            point, rows, polygon
        ])
    )

    print(parcel)

    print(upload(parcel))