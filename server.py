import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('localhost', 12345))

print("Weather Monitoring Server is waiting for data...")

while True:
    data, address = server.recvfrom(1024)

    temperature = data.decode()

    print("Temperature received:", temperature, "°C")
    print("Received from:", address)