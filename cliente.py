import socket

def cliente():
    host = '127.0.0.1'  # Cambia esto por la IP del servidor
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Conectado al servidor. Escribe mensajes para enviar (escribe 'salir' para terminar).")

    while True:
        mensaje = input(">> ")
        if mensaje.lower() == 'salir':
            break
        client_socket.sendall(mensaje.encode())

    client_socket.close()

if __name__ == "__main__":
    cliente()

