# UDP Chat Server
This project is a simple UDP-based chat server implemented in Python. It allows multiple clients to connect to a central server and communicate in real-time. The system uses sockets for network communication and threads to handle multiple clients concurrently.

## Features

Supports multiple clients simultaneously.

Requests a nickname from clients upon connection for identification.

Broadcasts messages from one client to all other connected clients.

**More features could be added to make it more robust and exception handling could be improved**

## How to Use

1. Clone the Repository
```bash
git clone https://github.com/jmoreno1852/UDP-Chat.git
cd UDP-Server/
```
2. Run the Server

  Ensure you have Python installed (version 3.8 or higher), then start the server:
```bash
python main.py
```
  The server will start and listen for incoming connections on port 4444 by default.

3. Run a Client

  Open multiple terminals and run:
```bash
python client.py
```
  Enter a nickname when prompted and start chatting. Messages will be visible to all connected clients.

## File Structure
```bash
📁 UDP-Chat/
│── 📁 src/
│   │── server.py   # Contains the main server logic
│   │── client.py   # Contains the client logic
│── main.py         # Entry point to start the server
│── README.md       # Project documentation
```

