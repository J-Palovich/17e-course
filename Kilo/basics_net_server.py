# This is based heavily on https://docs.python.org/3/library/socket.html#example

# We'll start by setting up a basic client and server:

# The server will wait to receive a message, and then will display it
# The client will transmit a message.
#########################################################################################################

# import socket

# print("Ready to receive a client connection.")
# HOST = ''                 # Symbolic name meaning all available interfaces
# PORT = 50007              # Arbitrary non-privileged port
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen(1)
#     conn, addr = s.accept()
#     print('Connected by', addr)
#     data = conn.recv(1024)
#     print(data.decode())
#     conn.close()

#########################################################################################################
# Makes communication bidirectional


import socket

print("Ready to receive a client connection.")
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr, 'and waiting for a message')
    while True:
        data = conn.recv(1024)
        print(data.decode())
        mymessage = input("What say? ")
        conn.sendall(mymessage.encode("UTF"))
        ## Notice that we do need to run `conn.close()` at some point.


#########################################################################################################








