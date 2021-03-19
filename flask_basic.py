from flask import Flask
app=Flask(__name__) # __name__ name of the module

@app.route("/home") # Browser url
def home():
	return " <h1> Home Page</h1> "

@app.route("/about")
def hello():
	return "<h1> About Page</h1>"


if __name__=='__main__':
	app.run(debug=True)