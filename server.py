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
	session['guessNumber'] = request.form['guessNumber']
	print "randon" , session['random_number']
	print "chosen" , session['guessNumber']
	if session['guessNumber'] == session['random_number'] :
		session['message'] = "Yes"
		session.pop('guessNumber')
		session.pop('random_number')
	elif session['guessNumber'] < session['random_number'] :
		session['message'] = "Too low"
		session.pop('guessNumber')
	else :
		session['message'] = "too high"
		session.pop('guessNumber')
	return render_template ('index.html', message=session['message'])


app.run(debug=True)