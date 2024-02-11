import socket
import sys


def connect_to_server(ip_address, port_num, message):
    # create a new socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((ip_address, int(port_num)))

        client_socket.sendall(message.encode())

        response = client_socket.recv(1024).decode()

        print(response)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    ip = sys.argv[1]
    port = sys.argv[2]
    msg = sys.argv[3]

    connect_to_server(ip, port, msg)
