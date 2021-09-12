#from database import Database, Note

def extract_route(string):

    inicio=string.index('/')+1

    final=string.index('HTTP')-1

    return string[inicio:final]

import os

def read_file(path):

    extensions = [".txt",".html", ".css", ".js"]

    name, extension = os.path.splitext(path)

    for i in extensions:

        if extension == i:

            t = open(path, "r")

            content = t.read()

            return content.encode()

    b = open(path, 'rb')

    content = b.read()

    return content

path='img/logo-getit.png'

#print(read_file(path))

import json

#from data import notes

def load_data(json_file):

    filePath = "data/"+json_file
    with open(filePath, "rt", encoding="utf-8") as text:
        content = text.read()
        contentPython = json.loads(content)
    
    return contentPython

def load_template(file):
    file= open('templates/'+file)
    content= file.read()
    file.close()

    return content

def add_note(new_note):

    notes=load_data('notes.json')
    notes.append(new_note)
    with open('data/notes.json','w') as note_new:
        json.dump(notes,note_new)

def del_note(note,db):

    database = Database('data/'+db)

    notes = database.get_all()

    for nota in notes:
        if ((nota.title == note.title) and (nota.content == note.content)):
            id=nota.id
    
    database.delete(id)

def build_response(body='', code=200, reason='OK', headers=''):

    if headers=='':
        return ('HTTP/1.1 '+str(code)+' '+reason+'\n\n'+body).encode()

    return ('HTTP/1.1 '+str(code)+' '+reason+'\n'+headers+'\n\n' +body).encode()
    
