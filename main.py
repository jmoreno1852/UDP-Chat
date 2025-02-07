import threading
from src.server import *
import sys
def main():
    host = "127.0.0.1"
    port = 4444

    s = setup_server(host, port)
    try:
        thread = threading.Thread(target=receive_data, args=(s,))
        thread.start()
    except KeyboardInterrupt:
        sys.close()
        
if __name__ == "__main__":
    main()
