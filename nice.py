from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html><a href='/hello'>Hi! This is the home page.</a><html>"


@app.route('/hello')
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
          <label>What's your name?
            <input type="text" name="person">
          </label>
          <br>
          <br>
          <label>What compliment would you like?<br>
            <input type="radio" name="nice" value="awesome">Awesome<br>
            <input type="radio" name="nice" value="terrific">Terrific<br>
            <input type="radio" name="nice" value="fantastic">Fantastic<br>
            <input type="radio" name="nice" value="neato">Neato<br>            
            <input type="radio" name="nice" value="fantabulous">Fantabulous<br>
            <input type="radio" name="nice" value="wowza">Wowza<br>           
            <input type="radio" name="nice" value="oh-so-not-meh">Oh-So-Not-Meh<br>
            <input type="radio" name="nice" value="brilliant">Brilliant<br>            
            <input type="radio" name="nice" value="ducky">Ducky<br>
            <input type="radio" name="nice" value="coolio">Coolio<br>            
            <input type="radio" name="nice" value="incredible">Incredible<br>
            <input type="radio" name="nice" value="wonderful">Wonderful<br>            
            <input type="radio" name="nice" value="smashing">Smashing<br>
            <input type="radio" name="nice" value="lovely">Lovely</label><br><br>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    nice_thing = request.args.get("nice")

    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, nice_thing)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
