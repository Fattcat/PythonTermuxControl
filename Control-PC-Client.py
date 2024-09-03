import socket

# Nastavenie klienta
SERVER_IP = '192.168.1.10'  # Zmeňte na IP adresu počítača so spusteným serverom
PORT = 12345                # Rovnaký port ako na serveri

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))
    print(f"Pripojený na server {SERVER_IP}:{PORT}")

    try:
        while True:
            command = input("Zadajte príkaz (napr. 'press win') alebo 'quit' pre ukončenie: ")
            if command.strip().lower() == 'quit':
                break

            client_socket.sendall(command.encode())

    finally:
        client_socket.close()
        print("Pripojenie ukončené")

if __name__ == "__main__":
    start_client()
