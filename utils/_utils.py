import socket
from .data import parse
class Serv:
    def __init__(self, ip, port=4444) -> None:
        self.serv = socket.socket()
        self.serv.bind((ip, port))
        self.started = False


    def serve(self):
        self.started = True
        self.serv.listen(1)