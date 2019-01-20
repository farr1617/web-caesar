from flask import Flask, request
from caesar import rotate_character
app = Flask(__name__)
app.config['DEBUG'] = True

form="""

<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="post">
  Rotate by: <input type="text" name="rot"><br>
  Submit Query: <input type="textarea" name="text"><br>
  <input type="submit" value="0">
</form> 
    </body>

</html> 
"""
@app.route("/", methods=['POST'])
def encrypt (text, rot):
    encrypted_text = ""
    for i in list(text):
      encrypted_text += rotate_character(i, rot)
    return '<h1>form.format(encrypted_text)</h1>'

@app.route("/")
def index():
    return form.format("")

app.run()