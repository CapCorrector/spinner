if __name__ == '__main__':
    import socket

    HOST, PORT = "127.0.0.1", 9998
    data = "get_cpu"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(5)
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))
        received = str(sock.recv(1024), "utf-8")
        sock.close()

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
