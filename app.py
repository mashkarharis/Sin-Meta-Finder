
import os
from flask import Flask , render_template, send_from_directory

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html', content="Hello World!")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'templates'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/styles.css')
def styles():
    return send_from_directory(os.path.join(app.root_path, 'templates'),
                          'styles.css',mimetype='text/css')


if __name__ == '__main__':
    app.run(debug=True)