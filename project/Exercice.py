from flask import Flask
from flask import request
from flask import make_response
import json
import os

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def getList():
    body = ""
    tab_body = []
    if request.method == "GET":
        counter = 0
        while True:
            try:
             #   with open(f'projet/users/{counter}.txt') as f:
                with open(f'users/{counter}.txt') as f:
                    lines = f.readlines()
                    count = 0
                    for line in lines:
                        count += 1
                        print(f'fichiers {counter} ligne {count}: {line}')
                        body = body + f'fichiers {counter} ligne {count}: {line} <br>'
                        test = tab_body.append(body)
                counter = counter + 1
            except IOError:
                return body

    print(f'arguments : {request.args}')
    print(f'body: {request.get_json()}')

    return make_response(body,200)



'''
- on delete un ficher txt pour delete un users 
- on import "os" 
- on va voir si le ficher existe 
- on remove le ficher si il existe sinon ou envoie un message d'erreur
'''


@app.route("/delete", methods=["GET", "DELETE"])
def delete():
    #on vérifie si le fichier existe ou non avant de le supprimer.

    if os.path.exists('users/2.txt'):
        os.remove('users/2.txt')
        return make_response("fichier 2 supprimé ", 200)
    else:
        return make_response("Impossible de supprimer le fichier car il n'existe pas", 404)




if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )
