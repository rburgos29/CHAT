import socket

IP = "10.108.33.28"
PORT = 8011

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

try:
    s.connect((IP, PORT))
except OSError:
    print("Socket already used")
    # But first we need to disconnect
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))


while True:
    cmensaje = input('Escriba aqui lo que desee enviar:')
    send_bytes = str.encode(cmensaje)
    s.send(send_bytes)
    msg =  s.recv(len(str(s))).decode("utf-8")
    if msg.lower() == 'salir':
        send_bytes = str.encode(msg)
        s.send(send_bytes)
        s.close()
        break
    print("Read from the SERVER:", msg)
