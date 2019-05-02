#!/usr/bin/env python3

import socket
import pymongo
from splitter import string_2_dict
import time


client = pymongo.MongoClient('mongodb://localhost:27017') #Pymongo client creation
sec_db = client['sec_db'] #Creation of security_database
patrol = sec_db['patrol'] #Creation of patrol collection

#Host and port declaration
host = '0.0.0.0' 
port = 7777

#TCP socket creation and putting in listen mode
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(10)

while True:
	
	client_socket, addr = server_socket.accept() #Get client socket and address
	print(f"Connection from {addr} established.")

	data = client_socket.recv(1024) #Recieve data by 1024 chunks
	if not data:
		client_socket.close() #If no data has been recieved from a client -> close connection
		break
	else:
		arr_of_docs = string_2_dict(data) #Custom function to decode, split data and add it to an array
		client_socket.send(b"Data has been recieved.") #Send confirmation message from the server
		db_result = patrol.insert(arr_of_docs) #Insert array of docs to a collection
		client_socket.close() #Close the client socket

server_socket.close() #Close the server socket