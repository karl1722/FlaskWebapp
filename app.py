from flask import Flask, render_template, url_for

app = Flask(__name__)

#define entry point, '/' = website root
@app.route('/')

#define root name
def index():
    #webpage content
    return render_template('index.html')


@app.route('/cats')
def cats():
    return 'Tinky, Buttons & Pouncer'

@app.route('/greeting/<name>/<salutation>')
def greeting(name, salutation):
    return render_template('page.html', name=name, salutation=salutation)

if __name__ == '__main__':
    #'0.0.0.0' means accessible by any device on network
    app.run(debug=True, host='0.0.0.0')

