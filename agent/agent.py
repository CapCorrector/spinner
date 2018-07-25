import psutil
import socketserver
import socket
import os

class Monitor(socketserver.BaseRequestHandler):
	def __init__(self):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
		    self.sock.connect((LHOST, LPORT))
		    self.sock.sendall(bytes(os.environ.get('HOSTIP') + "\n", "utf-8"))
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
		print("exiting")
	

if __name__ == "__main__":
	LHOST, LPORT = "10.0.0.200", 998
	HOST, PORT = "0.0.0.0", 999
	try:
		with socketserver.TCPServer((HOST, PORT), Monitor) as server:
			server.serve_forever()
	finally:
		Monitor.unregister("exiting")
	
