"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
    "smelly", "bone-headed", "stinky", "small", "puny", "a worm", "silly", 
    "mediocre", "leading a life of quiet desperation", "big-nosed", "you smell like wet dog",
    "inconsiderate", "abominable", "asinine", "a clown", "a blowhard"
]


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
        Hi! This is the home page.<br>
        <a href="/hello">Hello</a>
    </html>
    
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>

        <form action="/greet">
        What's your name? <input type="text" name="person">
        Choose a compliment <select name="compliment">
                <option value="awesome">awesome</option>
                <option value="terrific">terrific</option>
               <option value="fantastic">fantastic</option>
               </select>
         <input type="submit" value="Are you ready to be praised?">
        </form>

        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Are you ready to be insulted?">
        </form>
      </body>
    </html>
    """




@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    #compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!!
      </body>
    </html>
    """

    # f"""Hi, {player}! I think you're {compliment}!"""

@app.route("/diss")
def diss_person():

    player = request.args.get("person")
    diss = choice(INSULTS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
