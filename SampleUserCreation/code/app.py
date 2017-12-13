from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity
from users import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__': # This makes it such that this will not run if this file is imported, runs only if file is directly run
    app.run(debug=True)  # important to mention debug=True