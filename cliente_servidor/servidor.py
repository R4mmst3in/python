import socket
import threading

HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 65432

ADDR  = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")

	connected = True

	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)

		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			conn.send("Accepted connection...".encode(FORMAT))

			if msg == DISCONNECT_MESSAGE:
				connected = False
				conn.send("Disconnect accepted...".encode(FORMAT))

			print(f"[{addr}] {msg}")
			conn.send("Message received...".encode(FORMAT))
	conn.close()


def start():


	server.listen()

	while True:
		conn, addr = server.accept()

		thread = threading.Thread(target=handle_client, args=(conn, addr))

		thread.start()

		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print(f"[STARTING] server is starting on {SERVER}")

start()
