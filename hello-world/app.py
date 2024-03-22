from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def homepage():
    """View function for Home Page."""
    return "Paws Rescue Center 🐾"

@app.route("/about")
def about():
    """View function for About Page."""
    return """We are a non-profit organization working as an animal rescue center. 
    We aim to help you connect with the purrfect furbaby for you! 
    The animals you find at our website are rescue animals which have been rehabilitated. 
    Our mission is to promote the ideology of "Adopt, don't Shop"!"""

@app.route("/home")
def home():
    return "Welcome to the HomePage!"


@app.route("/educative")
def learn():
    return "Happy Learning at Educative!"


@app.route("/<my_name>")
def greatings(my_name):
    """View function to greet the user by name."""
    return "Welcome " + my_name + "!"


@app.route('/square/<int:number>')
def show_square(number):
    """View that shows the square of the number passed by URL"""
    return "Square of " + str(number) + " is: " + str(number * number)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
