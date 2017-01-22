from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from application import Applicants

app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def home():
    """Return Homepage"""

    return render_template('index.html')

@app.route("/application-form")
def application_form():
    """Return Application Form Page"""

    return render_template('application-form.html')

@app.route("/application-success", methods=["POST"])
def application_succss():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    salary = float(request.form.get("salary"))
    job = request.form.get("jobtype")
    new_applicant = Applicants(fname, lname, salary, job)
    """I know here that i could have just passed in fname, lname, 
    salary and job into the render_template. However I do believe it is import
    to create a class that every applicant is a instance of applicants, so later
    we can store those applications. Also, I wan to practice use class.
    """
    return render_template("application-response.html", new_applicant=new_applicant)
    


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
