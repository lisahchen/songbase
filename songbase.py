from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index ():
    # return '<h1>hello world!!!</h1>'
    return render_template('index.html')


@app.route('/my-songs')
def get_user(name):
    #return 'hello %s, your age is %d' % (name, 3)
    return render_template('user.html', user_name = name)


@app.route('/user/<string:name>/')
def get_user(name):
    #return 'hello %s, your age is %d' % (name, 3)
    return render_template('user.html', user_name = name)


@app.route('/songs')
def get_all_songs():
    songs = [
    'song 1',
    'song 2',
    'song 3'
    ]
    return render_template('songs.html', songs = songs)


@app.route('/users')
def show_all_users():
    return '<h2>this is the page for all users</h2>'


if __name__ == '__main__':
    app.run()
