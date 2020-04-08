#----- Inicio de appliacion
import os
import csv

clear= lambda: os.system('cls')
CLIENT_TABLE='.clients_info.csv'
CLIENT_SCHEMA=['name','company', 'email', 'position']
clients=[]
clear()

def _initialize_clients_from_storage():
    with open (CLIENT_TABLE,mode='r') as input_file:
        reader= csv.DictReader(input_file,fildnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    tmp_table_name='{}.tmp'.format(CLIENT_TABLE)
    with open (tmp_table_name, mode='w') as tem_file:
        writer= csv.DictWriter(tem_file,fieldnames=CLIENT_TABLE)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name,CLIENT_TABLE)


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
    _save_clients_to_storage()

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
   _initialize_clients_from_storage()

    with open('welcome_message.txt','r') as welcome_f:
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
# ---------GIT-----------------
# git config --global user.name ""
# ssh-keygen -t rsa -b 4096 -C "jsduenass@unal.edu.co"
# eval $( ssh-agent -s)         esta corriendo el agente ssh
# ssh-add ~/.ssh/id_rsa
# git location
# /e/Documentos/codigo/platzi/python/CRUD_app
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
# git  remote add origin  [url] 
# git remote -v
# git push origin master     git push [to_there] [from_here]
# git pull origin master    git pull [from_there] [to_here]
# git pull origin master --allow-unrelated-histories
# git remote set-url origin [ssh direction] git@github.com:jsduenass/CRUD_app.git
# alias git_history=git log --all --graph --decorate --oneline
# git tag -a v0.1 - m "commint message" [commit_id]
# git tag -d [tag_name]
#git push origin --tag

# gitk show branch history


#terminal.integrated.shell.* can only be defined in user settings and not at workspace scope
#git config --global core.editor "code"


