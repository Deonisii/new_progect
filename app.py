from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/sign')
def sign():
    return render_template ('registr.html')


if __name__ == "__main__":
    app.run(debug=True)
