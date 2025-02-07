import socket
import threading

nickname = input("Enter your nickname: ")
server = ('127.0.0.1',4444)
#Connect to server

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.sendto(f"Name: {nickname}".encode('utf-8'),server)

def receive(c):
    while True: 
        try:
            message, addr = c.recvfrom(1024)
            decoded_message = message.decode('utf-8')
            print(decoded_message)
        except Exception as e:
            print(e)
            break

def write(c):
    while True:
        message = '{}: {}'.format(nickname, input(''))
        c.sendto(message.encode('utf-8'),server)
#Main

receive_thread = threading.Thread(target=receive, args=(c,))
receive_thread.start()

write_thread = threading.Thread(target=write, args=(c,))
write_thread.start()
