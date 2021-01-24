from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)

    # This option will cause Jinja to throw UndefinedErrors if a value hasn't
    # been defined (so it more closely mimics Python's behavior)
            # *** what is the value of StrictUndefined ?
app.jinja_env.undefined = StrictUndefined

# This option will cause Jinja to automatically reload templates if they've been
    # changed. This is a resource-intensive operation though, so it should only be
    # set while debugging.
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = 'ABC'


# dictionary containing info about the most-loved melons
MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}


# REPLACE THIS WITH YOUR ROUTES
# write a route for "top-melons"
@app.route("/top-melons")
# create a view function that will render template for top-melons.html
def view_top_melons():
    if "username" in session:
        #pass through the html template, the loved melons dictionary
        return render_template ("top-melons.html", 
                                username="username", 
                                loved_melons_dict=MOST_LOVED_MELONS)
    else:
        return redirect("/homepage.html")

@app.route("/")
def add_username():
    if "username" in session:
        return redirect("/top-melons")
    else:
        return render_template("homepage.html")

# FIX THE GET
@app.route("/get-name", methods=["GET"])
def get_name():
    # get the username and save to user_name variable
    username = request.args.get('username')
    # add variable to session
    session["username"] = username

    return redirect("/top-melons")

    



if __name__ == '__main__':
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
