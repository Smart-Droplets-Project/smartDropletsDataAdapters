from ngsildclient import Client


class DAClient:

    __instance: Client = None


    @classmethod
    def get_instance(cls, host: str = None, port: int = None) -> Client:
        if cls.__instance is None:
            if host is not None and port is not None:
                cls.__instance = Client(host, port)
            else:
                cls.__instance = Client()
        return cls.__instance