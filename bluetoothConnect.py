from bluetooth import *

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect(("24:DA:9B:73:EE:A9", 3))

client_socket.send("Hello World")

print("Finished")

client_socket.close()