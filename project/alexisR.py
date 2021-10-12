from flask import Flask

app = Flask(__name__)

@app.route("/")

#
#fonction basic qui prend rien en paramêtre et renvoie <p>coucou</p>
#
def hello_world():
    return '<p>coucou</p>'

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True,
    )