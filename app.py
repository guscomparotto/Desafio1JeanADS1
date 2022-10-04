from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home1 ():
    return  render_template('index.html')

@app.route('/index')
def home ():
    return  render_template('index.html')

@app.route('/contato')
def contatos ():
    return  render_template('contato.html')

@app.route('/quem-somos')
def quemsomos ():
    return  render_template('quem-somos.html')