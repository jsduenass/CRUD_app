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
    clients.append(client_name)

def delete_client():
    global clients
    list_clients()
    client_name= _get_client_name() 
    if client_name in clients:
        clients.remove(client_name)
        print('{} was succesfully deleted'.format(client_name))
    else:
        print('{} was not found on client list '.format(client_name))
    list_clients()

def update_client():
    global clients
    list_clients()
    client_name= _get_client_name() 
    if client_name in clients:
        index= clients.index(client_name)
        updated_client_name= input('{} was found, enter it\'s new name: '.format(client_name))
        clients[index]= updated_client_name
    else:
        print('{} was not found on client list unable to update'.format(client_name))
    list_clients()

def list_clients():
    global clients
    
    for idx ,client in enumerate(clients):
        print('{}: {}'.format(idx,client)) 
    

def save():
    global input_file
    global clients
    input_file.truncate(0)
    input_file.seek(0)
    formated_client_list=', '.join(clients)
    input_file.write(formated_client_list)

def not_valid():
    input('COMMAND NOT VALID PRESS ENTER AND TRY AGAIN')

def select(command,options):
    """ allowd to a function on a variable options [dir] which stores the functions names """
    command=command.upper()
    func = options.get(command, "not_valid")   # function selected based 
    return   func+'()'

def nothing():
    pass

def end():
    pass


#---------------MAIN--------------------------------
if __name__ == '__main__':
   
    welcome_f=open('welcome_message.txt','r')
    welcome_banner=welcome_f.read()

    input_file=open('list.txt','r+')
    input_text=input_file.read() 
    clients=input_text.split(', ')
    main_menu= { 'C': 'create_client', 'D': 'delete_client','L':'list_clients', 'U':'update_client','S': 'save','Q':'end'}
    yes_no={'Y':'save' , 'N': 'end'}
    while True:
        command= str(input(welcome_banner))
        clear()
        func=select(command,main_menu)
        if func=='end()':
            command=str(input('you are about to close the application. do you want to save changes? \n Yes\\No \n'))
            save_func=select(command,yes_no)         
            exec(save_func) 
            if save_func=='"not_valid':
                pass
            else:    
                break           
        exec(func) 
    pass

    print(clients)

    welcome_f.close()
    input_file.close()
    




# Notas 
# funcion dir() y help()  permite conocer todas la funciones que puede hacer una variable
# [inicio:final:paso]
# git location
# E/Documentos/codigo/platzi/python/CRUD_app
# git log --stat
# git status
# git diff [commit_id] [commit_id]
# git checkout [commit_id]
# git reset HEAD quita los archivos de stage
# git clone [url]
# git push enviar
# git fetch
# git merge
# git pull = fetch + merge
# branch experiment  rama experimental
# git switch experiment





