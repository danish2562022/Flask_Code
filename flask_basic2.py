from flask import Flask,render_template
app=Flask(__name__) # __name__ name of the module

posts=[
{
	'author':'MD Danish Anwer',
	'title': 'Machine learning blogpost I',
	'content': ' KNN implementation',
	'date_posted':'19-March-2021'
},
{
	'author':'MD Danish Anwer',
	'title':'Machine learning blogpost II',
	'content': ' Naive Bayes implementation',
	'date_posted':'19-March-2021'
}
]

@app.route('/')
@app.route("/home") # Browser url
def home():
	return render_template('home.html',posts=posts)

@app.route("/about")
def hello():
	return render_template('about.html',title='about')


if __name__=='__main__':
	app.run(debug=True)