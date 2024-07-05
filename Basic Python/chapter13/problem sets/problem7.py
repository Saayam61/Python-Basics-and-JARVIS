# 7. Explore the ‘Flask’ module and create a web server using Flask & Python. 
# (done in env2)

# pip install flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# makes the code runnable through run of vscode, wont run without this
app.run()