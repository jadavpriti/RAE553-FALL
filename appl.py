
from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'priti'

jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

if __name__ == '__main__':
    app.run()
