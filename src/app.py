from flask import Flask, render_template
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template('index.html')

# gender trends page
@app.route('/gender')
def gender():
    return render_template('gender.html')

# race trends page
@app.route('/race')
def race():
    return render_template('race.html')

# age trends page
@app.route('/age')
def age():
    return render_template('age.html')

# county page
@app.route('/county')
def county():
    return render_template('county.html')

# county page
@app.route('/aboutauthor')
def author():
    return render_template('aboutauthor.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8105, threaded=True, debug=True)