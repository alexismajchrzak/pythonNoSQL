import os
import os.path


from flask import Flask

app = Flask(__name__)

'''
:argument
file_name: string
nom: string
prenom: string

:return 
result: string
'''


@app.route("/", methods=["GET", "POST"])
def addUser():
    list: list[str] = os.listdir("users")
    print(list)
    file_name = input()
    nom = input()
    prenom = input()
    result = ''
    docreate = True
    for i in range(len(list)):
        if list[i] == file_name + '.txt':
            result = 'Error'
            docreate = False
            break
    if docreate == True:
        file = open(f'users/{file_name}.txt', "w")
        file.write(nom + "\n" + prenom)
        file.close()
        result = 'Success'

    return result


3

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )
