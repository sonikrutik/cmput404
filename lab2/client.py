import socket, sys
def create_tcp_socket():
    print('Creating socket')
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(f'Failed to create socket. Error code: {str(msg[0])}, Error message : {msg[1]}')
        sys.exit()
    print('Socekt created successfully')
    return s

def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try: 
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print('Hostname could not be resolved. Exciting')
        sys.exit()

    print (f' Ip address of {host}')
    return remote_ip

def send_data(serversocket, payload):
    print("sendign payload")
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print('Send Failed')
        sys.exit()
    print('Payload sent successfully')

def main():
    try:
        host = 'www.google.com'
        port = 80
        payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
        buffer_size = 4096

        #make the socket, get the ip and connect
        s = create_tcp_socket()

        remote_ip = get_remote_ip(host)

        s.connect((remote_ip, port))
        print (f'Socket Connected to {host} on ip {remote_ip}')

        #send the data
        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)

        #print the data
        full_data = b""
        while True: 
            data = s.recv(buffer_size)
            if not data:
                break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()
if __name__ == "__main__":
    main()
