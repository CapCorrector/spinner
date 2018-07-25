import socketserver

class Listener(socketserver.BaseRequestHandler):
	def __init__(self):
		pass

	def handle(self):
		self.data = str(self.request.recv(1024).strip(), "utf-8")
		print(self.data)
	

if __name__ == "__main__":
	HOST, PORT = "0.0.0.0", 998
	try:
		with socketserver.TCPServer((HOST, PORT), Monitor) as server:
			server.serve_forever()
	finally:
		print("exiting")
	