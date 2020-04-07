#----- Inicio de appliacion
import os
clear= lambda: os.system('cls')
clients=''
clear()

def create_client():
    client_name= input('Enter the client name: ') 
    new_client(client_name)

    print('{} was succesfully created'.format(client_name))

def new_client(client_name):
    """ Este es un texto de ayuda para esta funcion """
    global clients
    clients+=client_name+', '

def delete_client():
    client_name= input('Enter the client name: ') 

    print('{} was succesfully deleted'.format(client_name))

def list_clients():
    global clients
    list= clients.split(', ')
    for client in list:
        print(client)
    pass

def not_valid():
    input('COMMAND NOT VALID PRESS ENTER AND TRY AGAIN')

def select(argument):
    switcher = { 'c': 'create_client', 'd': 'delete_client', 'l':'list_clients', 'q':'end'}
    func = switcher.get(argument, "not_valid")
    return   func+'()'


if __name__ == '__main__':
    welcome_f=open('welcome_message.txt','r')
    welcome_banner=welcome_f.read()
    
    
    while True:
        command= str(input(welcome_banner))
        clear()
        func=select(command)
        if func=='end()':
            break
        exec(func) 
    pass






# Notas 
# funcion dir() y help()  permite conocer todas la funciones que puede hacer una variable
# git location
# E/Documentos/codigo/platzi/python/CRUD_app







