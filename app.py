import os
from flask import Flask, redirect, request, send_from_directory, url_for
from msal_flask_auth import FlaskAuth

app = Flask(__name__)

app.config.update(
    SECRET_KEY=os.getenv("SECRET_KEY"),
    MSAL_CLIENT_ID=os.getenv("CLIENT_ID"),
    MSAL_CLIENT_SECRET=os.getenv("CLIENT_SECRET"),
    MSAL_AUTHORITY="https://login.microsoftonline.com/" + os.getenv("TENANT_ID"),
    MSAL_REDIRECT_PATH="/signin-oidc"
)

auth = FlaskAuth(app)

@app.route('/')
def index():
    # Devolvemos un formulario HTML básico como string

    user = auth.get_user()
    
    return f'''
        <html>
            <body>
                <h1>Bienvenido {user}!</h1>
                <h2>Introduce tu valor</h2>
                <form action="/hello" method="post">
                    <input type="text" name="name">
                    <input type="submit" value="Enviar">
                </form>
            </body>
        </html>
    '''

# @app.route('/signin-oidc') # no hace falta, lo gestion la biblioteca msal-flask-auth
# def signin_oidc():
#         return f'''
#             <html>
#                 <body>
#                     <p>Recurso signin-oidc.</p>
#                     <a href="{url_for('index')}">Volver atrás</a>
#                 </body>
#             </html>
#         '''

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')

    if name:
        print('El valor recibido es %s' % name)
        # Devolvemos el parámetro dentro de un encabezado <h1> y un párrafo <p>
        return f'''
            <html>
                <body>
                    <h1>El valor recibido es {name}!</h1>
                    <a href="{url_for('index')}">Volver atrás</a>
                </body>
            </html>
        '''
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
