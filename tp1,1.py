from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
 return "hello h3"


@app.route('/ma_route/<name>')
def ma_route(name):
 return 'Hello %s' % name
@app.route('/maroute/<name>')
def maroute(name):
    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)