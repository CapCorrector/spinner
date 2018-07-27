import psutil
import socketserver
import socket
import os

class Monitor(socketserver.BaseRequestHandler):
	def register(self):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
		    self.sock.settimeout(5)
		    self.sock.connect((LHOST, LPORT))
		    self.sock.sendall(bytes("REG: " + os.environ.get('HOSTIP') + "\n", "utf-8"))
		    self.sock.close()
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
	def unregister(self):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
			self.sock.settimeout(5)
			self.sock.connect((LHOST, LPORT))
			self.sock.sendall(bytes("UNREG: " + os.environ.get('HOSTIP') + "\n", "utf-8"))
			self.sock.close()

if __name__ == "__main__":
	LHOST, LPORT = "10.0.0.200", 998
	HOST, PORT = "0.0.0.0", 999
	try:
		with socketserver.TCPServer((HOST, PORT), Monitor) as server:
			Monitor.register(server)
			server.serve_forever()
	finally:
		Monitor.unregister(server)
	
