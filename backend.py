from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/start_game', methods=['POST'])
def start_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    return jsonify({'secret_number': secret_number})

@app.route('/check_guess', methods=['POST'])
def check_guess():
    guess = int(request.json['guess'])
    secret_number = int(request.json['secret_number'])

    if guess < secret_number:
        result = 'low'
    elif guess > secret_number:
        result = 'high'
    else:
        result = 'correct'
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
