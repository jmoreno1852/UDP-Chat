import socket
import threading

#Variables globales
clients = [] #Lista de conexiones, en principio not needed? 

#Set server
def setup_server(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    print(f"\nServer listening on {host}:{port}")
    return s
#receive

def add(addr, nickname):
    global clients
    clients.append({ "addr": addr, "nickname": nickname})

def remove(nickname):
    global clients
    for client in clients[:]:
        if client['nickname'] == nickname:
            clients.remove(client)
            print(f"\nClient {nickname} removed")
            break
    else:
        print(f"\nClient {nickname} not found")

def broadcast(message,s):
    global clients 
    nickname, data = message.split(": ", 1)
    for client in clients:
        print(f"{client}")
        if client["nickname"] != nickname:
            try:
                s.sendto(message.encode('utf-8'),client["addr"])
            except:
                print(f"Could not send mesage to {client["nickname"]}")
        

def receive_data(s):
    global clients,user_counter
    while True:
        try:
            data, addr = s.recvfrom(1024)
            decoded_data = data.decode('utf-8')
            print(f"Decoded Data: {decoded_data}")
            if 'Name:' in decoded_data:
                nickname = decoded_data.replace("Name: ", "", 1)
                add(addr, nickname)
                print(f"User {nickname} logged!")
            else:
                broadcast(decoded_data,s) #has format <Name>: Data, strip name to match client[], 
                                        #Dont broad cast to emitter of message

        except:
            print("Receive data Error")
            break
            
