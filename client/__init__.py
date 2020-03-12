import docker
import logging

class Client:
    __connection = None

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        
    def new_connection(self) -> bool:
        try:
            self.__connection = docker.from_env()
            return True

        except Exception as err:
            logging.error(f'Docker connection failed: {err}')
            
        return False
