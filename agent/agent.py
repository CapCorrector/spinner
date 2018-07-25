import psutil
import socketserver

class Monitor(socketserver.BaseRequestHandler):
	def check_cpu(self):
		return str(psutil.cpu_percent(interval=1))

	def check_mem(self):
		return str(psutil.virtual_memory().percent)

	def handle(self):
		self.data = str(self.request.recv(1024).strip(), "utf-8")
		if self.data == "get_cpu":
			self.request.sendall(bytes(self.check_cpu(), "utf-8"))
		elif self.data == "get_mem":
			self.request.sendall(bytes(self.check_mem(), "utf-8"))
		else:
			self.request.sendall(bytes("BAD REQUEST\n", "utf-8"))

if __name__ == "__main__":
	HOST, PORT = "localhost", 999
	with socketserver.TCPServer((HOST, PORT), Monitor) as server:
		server.serve_forever()

	
