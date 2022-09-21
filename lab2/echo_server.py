import socket
import time

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #Question 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #bind socket to adress
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)

        print('Listening...')

        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)

            #recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

if __name__ == "__main__":
    main()