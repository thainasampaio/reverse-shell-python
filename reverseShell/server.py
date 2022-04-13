import threading 
import socket
import os

clients = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ip = 'localhost'
        porta = 80
        server.bind((ip, porta))
        server.listen(10)
        print(f"Ouvindo no ip {ip} na porta {porta}")
    except  Exception as ex:
        return print(f'\n Não foi possível iniciar o servidor: {str(ex)}.\n')

    while True:
        client, addr = server.accept()
        print(addr)
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            send_for_all_clients(msg, client)
        except:
            deleteClient(client)
            break

def send_for_all_clients(msg, c_client):
    for client in clients:
      if client != c_client:
        try:
            client.send(msg)
        except:
            deleteClient(client)

def deleteClient(client):
    client.close()
    clients.remove(client)

main()