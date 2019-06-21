from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            Rotate by: 
            <input name="rot" value={1}>
                <textarea name="text">{0}</textarea>
            </input>
            <input type="submit"></input>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("Type something here", "0")

@app.route("/", methods=['POST'])
def encrypted():
    rotation = int(request.form.get("rot"))
    text = request.form.get("text")
    encrypted_text = rotate_string(text, rotation)
    return form.format(encrypted_text, rotation)


app.run()