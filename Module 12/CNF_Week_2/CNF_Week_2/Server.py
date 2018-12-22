import socket
import csv

s = socket.socket()
host = '10.3.12.198'
port = 5001
s.bind((host, port))
s.listen(1)
rollno = []
dicti = {}

def Main():

    with open('data.csv', 'r') as file:
        read = csv.reader(file)
        for each in read:
            roll = each[0];
            secretques = each[1];
            ans = each[2];
            rollno.append(each[0])
            dicti[each[0]] = each[1]
    print("server ready")
while True:
    c, addr = s.accept()
    print("connected from:" + str(addr))
    data = c.recv(1024).decode()
    data = data.split(" ")
    if (data[0] == "MARK-ATTENDANCE"):
        for client in rollno:
            if client != data[1]:
                print("ROll not found")
            else
                message = "SECRETQUESTION"+"-"+dicti(client)
                s.send(message.encode())
    s.close()
if __name__ == '__main__':
    Main()