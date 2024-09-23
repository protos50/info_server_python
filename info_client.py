import socket
import json

def receive_full_data(sock):
    buffer_size = 4096
    data = b""
    while True:
        part = sock.recv(buffer_size)
        data += part
        if len(part) < buffer_size:  # Si recibimos menos del buffer_size, es el último fragmento
            break
    return data

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 55355))  # Conectar a localhost en el puerto 12345

    response = receive_full_data(client_socket)
    formatted_response = json.loads(response.decode('utf-8'))  # Decodificar y cargar JSON

    # Imprimir con formato legibles
    print("Respuesta del servidor:")
    print(json.dumps(formatted_response, indent=4))  # Formatear con indentación

    client_socket.close()

if __name__ == "__main__":
    main()
