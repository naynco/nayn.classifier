from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def suggest():
    title = request.args.post("title", "")
    return f'{escape(title)}!'
    
if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')