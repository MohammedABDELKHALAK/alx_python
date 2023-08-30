from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    processed_text = escape(text).replace('_', ' ')
    return f"C {processed_text}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python_text(text):
    processed_text = escape(text).replace('_', ' ')
    return f"Python {processed_text}"

@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def show_number_template(n):
    if isinstance(n, int):
        return render_template('number_template.html', number=n)
    else:
        return "Not a valid integer."

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def show_number_odd_or_even(n):
    if isinstance(n, int):
        odd_or_even = "even" if n % 2 == 0 else "odd"
        return render_template('/6-number_odd_or_even.html', number=n, odd_or_even=odd_or_even)
    else:
        return "Not a valid integer."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
