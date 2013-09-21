from flask import Flask
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def test():
    resp = twilio.twiml.Response()
    resp.message("asdf")
    return str(resp)

    return app

if __name__ == "__main__":
    app.run(debug=True)
