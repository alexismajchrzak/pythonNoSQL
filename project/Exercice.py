from flask import Flask
from flask import request
from flask import make_response
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def getList():
    body = ""
    tab_body = ["","","",""]
    if request.method == "GET":
        counter = 0
        while True:
            try:
                with open(f'users/{counter}.txt') as f:
                    lines = f.readlines()
                    count = 0
                    for line in lines:
                        count += 1
                        print(f'fichiers {counter} ligne {count}: {line}')
                        body = body + f'fichiers {counter} ligne {count}: {line} <br>'
                        tab_body[counter] = body
                counter = counter + 1
            except IOError:
                return body


    elif request.method == "POST":
        pass

    print(f'arguments : {request.args}')
    print(f'body: {request.get_json()}')

    return make_response(body,200)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )
