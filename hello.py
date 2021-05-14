from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc')
def hello():
    a = request.args.get('a')
    b = request.args.get('b')
    c = int(a) + int(b)
    return render_template('result.html', calculated_c=c)

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
