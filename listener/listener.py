import socketserver

ENCODING = "utf-8"

class Listener(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = str(self.request.recv(1024).strip(), ENCODING)
        print(self.data)
    

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 998
    try:
        with socketserver.TCPServer((HOST, PORT), Listener) as server:
            server.serve_forever()
    finally:
        print("exiting")
    
