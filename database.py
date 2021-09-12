import sqlite3

from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''


class Database:

    def __init__(self,nome):
        self.nome=nome
        self.conn=sqlite3.connect(self.nome+'.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY,title STRING, content STRING NOT NULL);')

        

    def add(self,note):
        self.conn.execute(f"INSERT INTO note (title,content) VALUES ('{note.title}','{note.content}');")
        self.conn.commit()

    def get_all(self):

        cursor = self.conn.execute("SELECT id, title, content FROM note")

        list=[]
        for linha in cursor:
            self.id=linha[0]
            self.title=linha[1]
            self.content=linha[2]
            list.append(Note(id=self.id,title=self.title,content=self.content))

        
            
        return list
        
    def update(self, entry):

        self.conn.execute(f"UPDATE note SET title = '{entry.title}' WHERE id = {entry.id}")
        self.conn.execute(f"UPDATE note SET content = '{entry.content}' WHERE id = {entry.id}")
        self.conn.commit()

    def delete(self, note_id):

        self.conn.execute(f"DELETE FROM note WHERE id = {note_id}")
        self.conn.commit()