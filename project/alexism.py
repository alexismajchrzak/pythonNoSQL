'''
- création commande flask
- renvoyer hello world
'''

#from flask import Flask
from flask import request
from flask import make_response

#app = Flask(__name__)


#@app.route("/")
#def hello_world():
 #   return "<p>Hello, World!</p>"





#app = Flask(__name__)


#@app.route("/user", methods=["GET","POST"])
#def hello_wrod():

 #   if request.method == "GET":
   #     pass
  #  elif request.method == "POST":
    #    pass

   # print(f"arguments : {request.args}")
   # print(f"body : {request.get_json}")

   # body = "Hello, World!"
    #return make_response(body, 200)


from flask import Flask
from flask import request
from flask import make_response
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_wold():
    if request.method == "GET":
        for i in range(3):
            with open(f'users/{i+1}.txt') as f:
                lines = f.readlines()
                count = 0
                for line in lines:
                    count += 1
                    print(f'line {count}: {line}')

    elif request.method == "POST":
        pass

    print(f'arguments : {request.args}')
    print(f'body: {request.get_json()}')

    body = f'line {count}: {line}'
    return make_response(body, 200)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )
