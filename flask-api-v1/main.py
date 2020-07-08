import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "This is V1 version "

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')