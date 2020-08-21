from flask import Flask, render_template, send_from_directory
#from os import listdir
#from os.path import isfile, join, dirname
import os

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/served/<served_file>')
def root(served_file):
    current_dir = os.getcwd()
    served_dir = f"{current_dir}/served"
    return send_from_directory(served_dir, served_file)

@app.route('/served')
def served():                                                                   
    onlyfiles = [f for f in os.listdir('served') if os.path.isfile(os.path.join('served', f))]
    return render_template("serving.html", files=onlyfiles)

if __name__ == "__main__":
    app.run(port=2224, host="0.0.0.0")
