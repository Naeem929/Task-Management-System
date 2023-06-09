import socket


def server_program():
    # get the hostname
    host = '192.168.10.121'
    port = 3003  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(2024).decode()
        # print("from connected user: " + str(data))
        words=[]
        b=''
        for i in data:
            if i=='+':
                words.append(b)
                b=''
            else:
                b=b+i
        words.append(b)
        print("ID: "+ str(words[0])) 
        print("Task: " + str(words[1]))
        print("Assignee: " + str(words[2]))
        print("Assigner: " + str(words[3]))


    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()