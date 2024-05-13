"""
 Example how to set up DAClient.
 DAClient is a singleton pattern for Client from ngsildclient package
 localhost:1026 are the default values for Client
 You can change them
"""
from sd_data_adapter.client import DAClient

if __name__ == '__main__':
    HOST: str = "localhost"
    PORT: int = 1026
    DAClient.get_instance(HOST, PORT)