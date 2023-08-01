from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    welcome = '<h1>Olá, programadores!</h1>'
    link = '<p><a href="user/Usuário">Clique aqui!</a></p>'
    return welcome + link


@app.route('/user/')
@app.route('/user/<name>')
def hello_world(name='Usuário'):
    personalize = f'<h1>Olá, {name}!</h1>'
    instruction = '<p>Altere o nome no <em>endereço do browser</em> e recarregue a página.</p>'
    return personalize + instruction


if __name__ == '__main__':
    app.run(debug=True)
