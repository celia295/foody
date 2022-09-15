from bottle import route, template, run, static_file


@route('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./assets/')


# Page d'accueil
@route('/')
def index():
    return template('templates/index.tpl')


"""
On ouvre un serveur en local sur le port 7000
Tapez http://localhost:7000/ dans le navigateur pour accéder au site après
avoir exécuté ce programme Python.
"""
if __name__ == "__main__":
    run(reloader=True, debug=True, host="127.0.0.1", port=7000)
