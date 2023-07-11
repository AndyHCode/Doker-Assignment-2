import json
import random
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    questions = [
    "Why don't scientists trust atoms?",
    "What did one wall say to the other wall?",
    "Why don't skeletons fight each other?",
    "What's the best thing about Switzerland?",
    "Why did the scarecrow win an award?",
    "How do you organize a space party?",
    "Why don't eggs tell jokes?",
    "What do you call a bear with no teeth?",
    "Why did the bicycle fall over?",
    "Did you hear about the mathematician who's afraid of negative numbers?"
    ]
    answers = [
    "Because they make up everything!",
    "I'll meet you at the corner!",
    "They don't have the guts!",
    "I don't know, but the flag is a big plus!",
    "Because he was outstanding in his field!",
    "You 'planet'!",
    "Because they might crack up!",
    "A gummy bear!",
    "It was two-tired!",
    "He will stop at nothing to avoid them!"
    ]
    num = random.randint(0, len(questions)-1)
    return json.dumps({f'Question':questions[num], 'Answer':answers[num]})

@app.route('/joke')
def joke():
    questions = [
    "Why don't scientists trust atoms?",
    "What did one wall say to the other wall?",
    "Why don't skeletons fight each other?",
    "What's the best thing about Switzerland?",
    "Why did the scarecrow win an award?",
    "How do you organize a space party?",
    "Why don't eggs tell jokes?",
    "What do you call a bear with no teeth?",
    "Why did the bicycle fall over?",
    "Did you hear about the mathematician who's afraid of negative numbers?"
    ]
    answers = [
    "Because they make up everything!",
    "I'll meet you at the corner!",
    "They don't have the guts!",
    "I don't know, but the flag is a big plus!",
    "Because he was outstanding in his field!",
    "You 'planet'!",
    "Because they might crack up!",
    "A gummy bear!",
    "It was two-tired!",
    "He will stop at nothing to avoid them!"
    ]
    source = request.args.get('num', type=int, default=0)
    tempList = []
    for _ in range(source):
        num = random.randint(0, len(questions)-1)
        tempList.append(questions[num] + " " + answers[num])
    return jsonify(jokes = tempList)



