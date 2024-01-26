from flask import Flask, request;


app = Flask(__name__);

@app.route("/api/welcome",methods=["GET"])
def get_welcome():
    return {
        "message" :"Welcome to flask application",
    }

@app.route("/api/members",methods=["POST","GET"])
def create_member(member):
    if request.method == "POST":
     data =request.get_json()
     


if  __name__ == "__main__":
    app.run(debug=True);