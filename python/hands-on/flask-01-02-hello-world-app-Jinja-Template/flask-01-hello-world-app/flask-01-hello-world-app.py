from flask import Flask 

app = Flask(__name__) 

@app.route('/')
def hello(): 
    return "Hello World from Flask!"

@app.route('/second')
def second(): 
    return "this is second "
@app.route('/third/subthird')
def third(): 
    return "this is sub of third"
    
@app.route('/fourth/<string:id>')
def frt(id): 
    return f"this is the {id}"



if __name__ == '__main__': 
    app.run(debug=True,port=2000)
