from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            expression = request.form['expression']
            result = eval(expression)
        except Exception as e:
            result = 'Error: ' + str(e)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

