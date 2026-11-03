import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    temperature = input("Enter temperature reading: ")

    if temperature == "exit":
        break

    client.sendto(temperature.encode(), ('localhost', 12345))

    print("Temperature sent successfully")

client.close()