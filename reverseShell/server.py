import threading 
import socket
import os

from setuptools import Command

clients = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ip = 'localhost'
        porta = 80
        BUFFER_SIZE = 1024 * 128
        server.bind((ip, porta))
        server.listen(10)

        client, addr = server.accept()
        print(addr)
        clients.append(client)

        print(f"Ouvindo no ip {ip} na porta {porta}")

          #recebendo o diretório de trabalho atual do cliente
        cwd = client.recv(BUFFER_SIZE).decode()
        print("Diretório de trabalho atual:\n", cwd)

    except  Exception as ex:
        return print(f'\n Não foi possível iniciar o servidor: {str(ex)}.\n')



    while True:
       Command = input =(f"{cwd} $> ")

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
