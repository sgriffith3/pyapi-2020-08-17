from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/goodbye')
def goodbye():
    return "Goodbye Cruel World"


@app.route('/user/<user>')
def user(user):
    files = ["test01", "test02", "test03"]
    hosts = {"server1": ["website", "database"], "server2": ["backup_db", "developer_site"]}
    return render_template("user.html", files = files, user = user, hosts = hosts)



@app.route('/dogs')
def dogs(doggies=['poodle', 'mutt', 'boxer']):
    return render_template("dogs.html", pups=doggies)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
