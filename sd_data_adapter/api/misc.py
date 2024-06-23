from ..client import DAClient

def is_alive_check():
    '''
    Test the connection to the Orion Context Broker
    '''

    with DAClient.get_instance() as client:

        return client.is_connected()

