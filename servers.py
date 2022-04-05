import socket
import time

main_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY, 1)
main_socket.bind(('localhost',10000))
main_socket.setblocking(0)
main_socket.listen(5)
print('Создался сокет')

players_sockets = []
while True:

        try:
            new_socket,addr=main_socket.accept()
            print('подключился',addr)
            new_socket.setblocking(0)
            players_sockets.append(new_socket)
        except:
            print("Нет желающих войти в игру")
            pass


        for sock in players_sockets:
            try:
                data=sock.recv(1024)
                data=data.decode()
                print('Получил', data)
            except:
                pass


            for sock in players_sockets:
                try:
                    sock.send('Новое состояние игры'.encode())
                except:
                    players_sockets.remove(sock)
                    sock.close()
                    print('Отключился игрок')
        
        time.sleep(1)
        print(players_sockets)
        
    
    
    
