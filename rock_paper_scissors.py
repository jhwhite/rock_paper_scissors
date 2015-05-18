from flask import Flask
from flask import render_template
import random 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/rps/<choice>')
def rps(choice):
    options = ["rock", "paper", "scissors"]
    winner = "computer"
    player_choice = choice.lower()
    
    computer_choice = options[random.randint(0,2)]

    if player_choice == "rock" and computer_choice == "scissors":
        winner = "player"
    if player_choice == "scissors" and computer_choice == "paper":
        winner = "player"
    if player_choice == "paper" and computer_choice == "rock":
        winner = "player"
    
    return render_template("rps.html", winner=winner.capitalize(), player_choice=player_choice, computer_choice=computer_choice)

app.run(debug=True)
