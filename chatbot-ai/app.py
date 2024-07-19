from flask import Flask, render_template, request, jsonify
from data import get_response  # Import your function from data.py

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('chat.html')

# Route to handle chat logic
@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    response = get_response(user_input)  # Call your function to get response
    return jsonify({'response': response})  # Return response as JSON

if __name__ == '__main__':
    app.run(debug=True)
