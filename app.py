from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return('user_page - ' + name + ' - '+ str(id))


@app.route('/user_id')
def user_id():
    return render_template('user.html')


@app.route('/sign')
def sign():
    return render_template ('registr.html')


if __name__ == "__main__":
    app.run(debug=True)