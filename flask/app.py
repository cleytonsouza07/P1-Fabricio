from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://cleytonsouza476:ZmMqerzNgM7SU9V8@cluster0.lkecjq6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('user_list.html')

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('index'))
    return render_template('user_form.html')

@app.route('/user/delete/<username>')
def delete_user(username):
    mongo.db.users.delete_one({'username': username})
    return redirect(url_for('index'))

@app.route('/user/edit/<username>', methods=['GET', 'POST'])
def edit_user(username):
    user = mongo.db.users.find_one({'username': username})
    if request.method == 'POST':
        new_username = request.form['username']
        new_password = request.form['password']
        return redirect(url_for('index'))
    return render_template('user_form.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
