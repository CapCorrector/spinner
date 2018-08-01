import psutil
import socketserver
import socket
import os

class Monitor(socketserver.BaseRequestHandler):
    def register(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            sock.connect((LHOST, LPORT))
            sock.sendall(bytes("REG: " + os.environ.get('HOSTIP') + "\n", "utf-8"))
            sock.close()
    def _check_cpu(self):
        return str(psutil.cpu_percent(interval=1))

    def _check_mem(self):
        return str(psutil.virtual_memory().percent)

    def handle(self):
        data = str(self.request.recv(1024).strip(), "utf-8")
        if data == "get_cpu":
            self.request.sendall(bytes(self._check_cpu(), "utf-8"))
        elif data == "get_mem":
            self.request.sendall(bytes(self._check_mem(), "utf-8"))
        else:
            self.request.sendall(bytes("BAD REQUEST\n", "utf-8"))
    def verify_request(self, request, client_address):
        
    def unregister(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            sock.connect((LHOST, LPORT))
            sock.sendall(bytes("UNREG: " + os.environ.get('HOSTIP') + "\n", "utf-8"))
            sock.close()

if __name__ == "__main__":
    LHOST, LPORT = "10.0.0.200", 998
    HOST, PORT = "0.0.0.0", 999
    try:
        with socketserver.TCPServer((HOST, PORT), Monitor) as server:
            Monitor.register(server)
            server.serve_forever()
    finally:
        Monitor.unregister(server)
    
