from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """web-caesar.html"""

@app.route("/")
def index():
    return form


app.run()