import socket

def servidor():
    host = '0.0.0.0'  # Escucha en todas las interfaces
    port = 12345      # Puerto para escuchar

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Espera 1 conexión

    print(f"Servidor escuchando en {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Conexión establecida con {addr}")

    while True:
        data = conn.recv(1024)  # Recibe hasta 1024 bytes
        if not data:
            break
        print(f"Mensaje recibido: {data.decode()}")
        # Puedes responder aquí si quieres:
        # conn.sendall(b"Mensaje recibido")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    servidor()

