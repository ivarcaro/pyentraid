import os
from flask import Flask, redirect, request, send_from_directory, url_for

app = Flask(__name__)

@app.route('/')
def index():
    print('Request for index page received')
    # Devolvemos un formulario HTML básico como string
    return '''
        <html>
            <body>
                <h2>Introduce tu nombre</h2>
                <form action="/hello" method="post">
                    <input type="text" name="name">
                    <input type="submit" value="Enviar">
                </form>
            </body>
        </html>
    '''

@app.route('/signin-oidc')
def signin-oidc():
        return f'''
            <html>
                <body>
                    <h1>Hola, {name}!</h1>
                    <p>Recurso signin-oidc.</p>
                    <a href="{url_for('index')}">Volver atrás</a>
                </body>
            </html>
        '''

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')

    if name:
        print('Request for hello page received with name=%s' % name)
        # Devolvemos el parámetro dentro de un encabezado <h1> y un párrafo <p>
        return f'''
            <html>
                <body>
                    <h1>Hola, {name}!</h1>
                    <p>Este parámetro se ha recibido correctamente sin usar ficheros externos.</p>
                    <a href="{url_for('index')}">Volver atrás</a>
                </body>
            </html>
        '''
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
