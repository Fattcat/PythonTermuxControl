import socket
import pyautogui

# Nastavenie servera
HOST = '0.0.0.0'  # Akceptuje pripojenia z akéhokoľvek hosta
PORT = 12345      # Zvolený port pre server

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server beží na {HOST}:{PORT} a čaká na pripojenie...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Pripojený klient: {addr}")

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            print(f"Prijatý príkaz: {data}")

            # Ak je prijatý príkaz 'press win', stlačíme Windows klávesu
            if data.strip().lower() == 'press win':
                pyautogui.hotkey('winleft')

        conn.close()
        print(f"Klient {addr} sa odpojil")

if __name__ == "__main__":
    start_server()
