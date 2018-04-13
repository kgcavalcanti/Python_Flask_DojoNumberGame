from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	import random
	session['random_number'] = random.randrange(0, 101)
	print session['random_number']
	return render_template ('index.html')

@app.route('/guess', methods=['POST'])
def guess():
	session['message'] = []
	session['guessNumber'] = int(request.form['guessNumber'])
	print "randon" , session['random_number']
	print "chosen" , session['guessNumber'], type(session['guessNumber'])
	if session['guessNumber'] == session['random_number'] :
		session['message'] = "Yes"
	elif session['guessNumber'] < session['random_number'] :
		session['message'] = "Too low"
		session.pop('guessNumber')
	elif session['guessNumber'] > session['random_number'] :
		session['message'] = "Too high"
		session.pop('guessNumber')
	return render_template ('index.html', message = session['message'])

@app.route('/tryAgain')
def tryAgain():
	session.pop('random_number')
	return redirect ('/')

app.run(debug=True)