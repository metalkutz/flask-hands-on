from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Function to generate chatbot responses
def generate_response(user_input):
    # Add your chatbot logic here
    return f"Chatbot: you said {user_input}"


# Define the home route
@app.route("/")
def home():
    return render_template("index.html")


# Define the route for handling user input
@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    response = generate_response(user_input)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
