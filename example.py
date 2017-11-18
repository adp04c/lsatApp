import os
from flask import Flask, render_template, request, redirect, jsonify
from react.render import render_component

DEBUG = True

app = Flask(__name__)
app.debug = DEBUG

comments = []
components_path = os.path.join(os.path.dirname(__file__),'static', 'js', 'src')

def path(js_file):
    return os.path.join(components_path, js_file)

@app.route('/')
def index():
    store = {'component': 'CommentBox.jsx'}
    store['props'] = {'comments': comments}

    rendered = render_component(
        os.path.join(os.getcwd(), 'flaskProj','project','static', 'js', path(store['component'])),
        {
            'comments': comments,
            'url': '/comment/',
        },
        to_static_markup=True,
    )

    store2 = {'component': 'banner.jsx'}
    rendered2 = render_component(
        os.path.join(os.getcwd(), 'flaskProj','project','static', 'js', path(store2['component'])),
        to_static_markup=True,
    )
    return render_template('index.html',
            rendered2= rendered2,
            rendered= rendered,
            store2=store2,
            store=store)



@app.route('/comment/', methods=('POST',))
def comment():
    comments.append({
        'text': request.form['text'],
    })
    texty= request.form['text']
    file = open(components_path +"/testy.txt","w")
    file.write(texty)
    file.close
    return jsonify({'comments': comments})

# Sample structure of the data
laws = [
    {
        'name': 'contracts',
        'statements' = [
            {
                'name': 'acceptance',
                'definition': 'SOME TEXT'
            }
        ]
    },
    {
        'name': 'torts',
        'statements' = [
            {
                'name': 'negligence',
                'definition': 'SOME TEXT'
            }
        ]
    },
    {
        'name': 'criminal'
    }
]

# allowing users to create contracts black letter law statements
@app.route('/contracts/', methods=('POST','GET'))
def define_contracts(name):
    request_data = request.get_json()
    new_definition = {
        'name': request_data['name'],
        'definition':   # Need to figure out how to have this be the user input as the definition
    }
    laws.append(new_definition)
    return jsonify(new_definition)

# User can view their definition of a contracts statement definition
@app.route('/contracts/<string:name>/define', methods=('GET'))
def get_contracts_statements(name):
    # iterate over the list of legal statements and find the right one
    for area_of_law in laws:
        if area_of_law['name'] == name:
            return jsonify({'statements' : area_of_law['statements']})
    return jsonify({'message' : 'statement not found'})

# Users practice writing the definition
@app.route('/contracts/<string:name>/practice', methods=('POST','GET'))
def get_contracts_statements(name):
    # iterate over the list of legal statements and find the right one
    for area_of_law in laws:
        if area_of_law['name'] == name:
            return jsonify({'statements' : area_of_law['statements']})
    return jsonify({'message' : 'statement not found'})

# Here we need another function that allows the user to give input, this is 
# where the user will practice re-typing the rule statement
def practice_statement():
    pass

@app.route('/clear/')
def clear():
    comments = []
    return jsonify({'comments': comments})


if __name__ == '__main__':
    app.run()
