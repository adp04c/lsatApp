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


@app.route('/clear/')
def clear():
    comments = []
    return jsonify({'comments': comments})


if __name__ == '__main__':
    app.run()
