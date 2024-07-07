# Importando a classe Flask da biblioteca flask
from flask import Flask

# Criação de uma variável app que receberá uma instância de Flask
# default configuration
app = Flask(__name__)

# Definindo uma rota raiz (página inicial)  a função que será executada ao requisitar
@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)