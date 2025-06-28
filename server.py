import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to address and port
host = '127.0.0.1'
port = 12346
server_socket.bind((host, port))
server_socket.listen(1)

print("🔌 Waiting for connection...")
conn, addr = server_socket.accept()
print(f"✅ Connected to {addr}")

# Chat loop
while True:
    message = conn.recv(1024).decode()
    if message.lower() == 'exit':
        print("Client has left the chat.")
        break
    print("Client:", message)
    reply = input("You: ")
    conn.send(reply.encode())
    if reply.lower() == 'exit':
        break

conn.close()
