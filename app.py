from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL(app)

@app.route('/')
def home1 ():
    return  render_template('index.html')

@app.route('/index')
def home ():
    return  render_template('index.html')

#contato sofre alteração devido ao formulário
@app.route('/contato', methods=['GET', 'POST'])
def contatos ():
    if request.method == "POST":  #se o usuário requisitar o método post
        email = request.form['email'] #pega a informação que um usuário está preenchendo
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor() #abre a conexão com o banco
        cur.execute('insert into contatos (email, assunto, descricao) values (%s, %s, %s)', (email, assunto, descricao)) #executa o insert into
        #%s = string  
        #primeiro campo assunto descricao = variação de carcteres na tabela
        #segundo campo = onde será inserido os dados

        mysql.connection.commit() #commita as informações do usuário
        cur.close() #fecha o post

        return 'sucesso'
    return  render_template('contato.html')

@app.route('/quem-somos')
def quemsomos ():
    return  render_template('quem-somos.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    users = cur.execute('SELECT * FROM contatos')
    
    if users > 0: #só entra no fetchall caso haja pelo menos um usuário
        userDetails = cur.fetchall()

    return render_template('user.html', userDetails=userDetails) #tabela #for html
    