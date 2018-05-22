from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/set")
def setcookie():
	resp = make_response('Seting Cookie!')
	resp.set_cookie('framework','flask')
	return resp

@app.route("/get")
def getcookie():
	framework = request.cookies.get('framework')
	return 'The framework is ' + framework

if __name__ == '__ main__':
	app.run(debug = True)
app.run(host = '0.0.0.0',port = 5000)
