from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdfñlkj2340987#"
socketio = SocketIO(app)


@app.route("/")
def session():
    return render_template("session.html")


def messageReceived(methods=["GET", "POST"]):
    print("message was received!!!")


@socketio.on("my event")
def handle_my_custom_event(json_data, methods=["GET", "POST"]):
    print("recieved json: " + str(json_data))
    socketio.emit("my response", json_data, callback=messageReceived)


if __name__ == "__main__":
    socketio.run(app, debug=True)
