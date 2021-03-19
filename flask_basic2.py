from flask import Flask
app=Flask(__name__) # __name__ name of the module

@app.route("/") # Browser url
def Hello():
	return "Hello World"