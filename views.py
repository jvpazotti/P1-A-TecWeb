from utils import load_data, load_template, build_response,add_note,del_note
from os import error, replace
from utils import load_data, load_template
import urllib
from database import Note,Database

data = Database('dados')

def index(request):

    note_template = load_template('components/note.html')

    notes_li = [
        note_template.format(id=dados.id,title=dados.title, details=dados.content)
        for dados in data.get_all()
    ]

    notes = '\n'.join(notes_li)
    
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus

        #titulo=Sorvete+de+banana 
        #detalhes=Coloque+uma+banana+no+congelador+e+espere.+Pronto%21+1%2B1%3D
        for chave_valor in corpo.split('&'):
            key, value = chave_valor.split("=")
            params[urllib.parse.unquote_plus(key)] = urllib.parse.unquote_plus(value)

        if params["post"]=="postar":
            note = Note(title = params["titulo"], content = params["detalhes"])
            data.add(note)
        
        if params['post']=='deletar':
            data.delete(params['id'])

        if params['post']=='editar':
            note = Note(id=params['id'],title = params["newtitle"], content = params["newdetails"])
            data.update(note)
    
        return (build_response(code=303, reason='See Other', headers='Location: /', body=load_template('index.html').format(notes=notes)))

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

    return build_response(body=load_template('index.html').format(notes=notes))
            