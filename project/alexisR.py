from flask import Flask
from flask import request
from flask import make_response
import json

app = Flask(__name__)
@app.route("/", methods=["get","post"])

#
#fonction get and post, elle n'a pas d'entrée mais renvoie hello world + le nombre de la réponse réseaux 
#
def json_file():
    if request.method == "get":
        pass
    elif request.method == "post":
        pass

    print(f'arguments : {request.args}')
    print(f'body: {request.get_json()}')
    
    return make_response(read(), 200)
with open('users/1.txt') as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1
            a = f'line {count}: {line}'
#
#fonction read qui lis le text d'un fichier, elle ne prend aucun paramêtre mais renvoie un
#objet composé d'un nom et d'un prénom
#
def read():
    
        
    
    return 
    
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True,
    )