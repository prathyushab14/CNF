import socket

def Main():
	host = '10.3.12.198'
	port = 5001

	s = socket.socket()
	s.connect((host, port))
	message = input("->")
	while (message != "quit"):
		s.send(message.encode())
		message = input()
	s.close()
def receivemsg(sock):
	while True:
		msg = sock.recv(1024).decode()
		print(msg)
	threading.Thread(target=receiveMsg,args=(s,)).start()
if __name__ == '__main__':
	Main()
