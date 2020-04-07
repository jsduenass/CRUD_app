#----- Inicio de appliacion
import os
clear= lambda: os.system('cls')
clients=''
clear()

def _get_client_name():
    return input('Enter the client name: ')

def create_client():
    client_name= _get_client_name() 
    new_client(client_name)

    print('{} was succesfully created'.format(client_name))

def new_client(client_name):
    """ Este es un texto de ayuda para esta funcion """
    global clients
    clients+=client_name+', '

def delete_client():
    global clients
    client_name= _get_client_name() 
    if client_name in clients:
        clients=clients.replace(client_name+', ', '')
        print('{} was succesfully deleted'.format(client_name))
    else:
        print('{} was not found on client list '.format(client_name))
    list_clients()

def update_client():
    global clients
    list_clients()
    client_name= _get_client_name() 
    if client_name in clients:
        updated_client_name= input('{} was found, enter it\'s new name: '.format(client_name))
        clients=clients.replace(client_name, updated_client_name)
    else:
        print('{} was not found on client list unable to update'.format(client_name))
    list_clients()

def list_clients():
    global clients
    list= clients.split(', ')
    for client in list:
        print(client)
    pass

def not_valid():
    input('COMMAND NOT VALID PRESS ENTER AND TRY AGAIN')

def select(argument):
    switcher = { 'C': 'create_client', 'D': 'delete_client','L':'list_clients', 'U':'update_client', 'Q':'end'}
    func = switcher.get(argument, "not_valid")
    return   func+'()'


if __name__ == '__main__':
   
    welcome_f=open('welcome_message.txt','r')
    welcome_banner=welcome_f.read()
    input_file=open('list.txt','r+')
    clients=input_file.read() 
    main_menu= { 'C': 'create_client', 'D': 'delete_client','L':'list_clients', 'U':'update_client', 'Q':'end'}
    
    while True:
        command= str(input(welcome_banner))
        command=command.upper()     # account for lower case
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







