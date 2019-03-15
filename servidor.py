import socket

PORT = 8011
IP = "10.108.33.28"
MAX_OPEN_REQUESTS = 5



def process_client(clientsocket):
    print(clientsocket)
    while True:
        msg =  clientsocket.recv(len(str(clientsocket))).decode("utf-8")
        if msg.lower() == 'salir':
            send_bytes = str.encode(msg)
            clientsocket.send(send_bytes)
            clientsocket.close()
            break
        print("Read from the CLIENT:", msg)
        smensaje = input('Escriba aqui lo que desee enviar:')
        send_bytes = str.encode(smensaje)
        clientsocket.send(send_bytes)





# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
# Let's use better the local interface name
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
