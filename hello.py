from flask import Flask, url_for, request
app = Flask(__name__)

#@app.route defines the url route and the code below what is returned.
@app.route("/")
def index():
    return "Index page!"

@app.route("/hello")
def hello():
    return "Hello world!"

#variable rules for the url search input
@app.route("/<user>")
def user(user):
    #this is the return to the body
    return 'User %s' % user

#URL building -- We pass the content of the function to be defined later
@app.route("/login")
def login(): pass
#Unknown elements from the url are appended as query parameters
@app.route("/profile/<username>")
def profile(username): pass

#url_for method
with app.test_request_context():
    print url_for("login")
    print url_for("profile", username="John Doe")

#HTTP methods
@app.route("/login2")
def login2():
    if request.method == "POST":
        return "Do the Login stuff"
    # case GET 
    else:
        return "Do the register stuff"

if __name__ == "__main__":
    app.run()
