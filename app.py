from flask import Flask, render_template, url_for, request
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/live', methods=['GET', 'POST'])
def live(new_game=GameOfLife(20, 20)):
    if new_game.counter > 0:
        new_game.form_new_generation()
    new_game.counter += 1
    return render_template('live.html', game=new_game)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
