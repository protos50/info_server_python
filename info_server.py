import socket
import json
import platform
import psutil
import os

def get_system_info():
    info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.architecture(),
        "hostname": platform.node(),
        "cpu": platform.processor(),
        "ram": f"{psutil.virtual_memory().total / (1024 ** 2):.2f} MB",
        "disk_usage": f"{psutil.disk_usage('/').percent} %",
        "partitions": psutil.disk_partitions(),
        "load_avg": os.getloadavg(),
        "network_interfaces": psutil.net_if_addrs(),
        "running_processes": [{"pid": p.info["pid"], "name": p.info["name"], "status": p.info["status"]} for p in psutil.process_iter(['pid', 'name', 'status'])]
    }
    return info

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 55355))
    server_socket.listen(5)
    print("Listening on localhost: 55355...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexión establecida con {addr}")

        system_info = get_system_info()
        response = json.dumps(system_info, indent=4)
        client_socket.send(response.encode('utf-8'))  
        client_socket.close()

if __name__ == "__main__":
    main()
