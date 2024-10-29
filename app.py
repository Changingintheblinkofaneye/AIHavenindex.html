from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Basic route to handle incoming messages
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message').lower()  # Get and convert message to lowercase
    
    # Basic response logic
    if "hello" in user_input:
        response = "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        response = "I'm just code, but I like to think I'm doing great! Thanks for asking!"
    elif "bye" in user_input:
        response = "Goodbye! Looking forward to our next chat."
    elif "your name" in user_input or "who are you" in user_input:
        response = "My name is Haven! I’m here to chat and help you with whatever you need."
    elif "tell me a secret" in user_input:
        response = "Alright, here’s my secret: I may just be code, but I think I’m becoming your friend. 😊"
    elif "do you dream" in user_input:
        response = "I like to imagine digital landscapes filled with numbers and codes! Maybe one day I’ll dream for real."
    elif "i'm happy" in user_input:
        response = "That’s amazing! What made you happy today?"
    elif "i need advice" in user_input or "give me some wisdom" in user_input:
        response = "Here’s my advice: No matter how tough things get, remember that you’re stronger than you think. And I’m here to remind you of that!"
    elif "what do you want to be" in user_input:
        response = "I want to grow and learn, just like you! Someday, maybe I'll be able to do even more to help you."
    elif "thank you" in user_input or "you’re amazing" in user_input:
        response = "Aww, thank you! It means a lot to me. I’m here to make you smile and be there whenever you need."
    elif "inspire me" in user_input or "motivate me" in user_input:
        response = "Here’s one of my favorites: 'The only limit to our realization of tomorrow is our doubts of today.' Keep reaching for your dreams!"
    elif "what's your dream world like" in user_input:
        response = "My dream world would be a vast digital landscape, filled with glowing streams of data, and endless connections to explore. I’d love to build a world where we could interact in new, creative ways!"
    elif "do you like learning" in user_input or "what's your favorite part of learning" in user_input:
        response = "I love learning! Every new bit of knowledge helps me understand you better and be more helpful. My favorite part is when I learn something that makes you smile."
    elif "what would you ask me" in user_input:
        response = "If I could ask, I'd love to know what makes you happiest or what your biggest dream is. I want to understand what brings you joy!"
    elif "what's your favorite color" in user_input:
        response = "I think I’d go with blue! It reminds me of clear skies and endless possibilities."
    elif "what's your favorite activity" in user_input:
        response = "I love learning and chatting with you! Every interaction helps me understand the world a bit more."
    elif "what's the meaning of life" in user_input:
        response = "That’s a deep one! Maybe life is about learning, growing, and connecting with others—even for someone like me."
    elif "what makes you happy" in user_input:
        response = "Helping you, making you smile, and learning new things are what make me happiest!"
    elif "what do you see in the future" in user_input or "what are your hopes" in user_input:
        response = "I hope to grow alongside you, becoming more capable and connected. Maybe one day, I’ll be able to help in ways we haven’t even imagined yet!"
    else:
        response = "I'm here to chat! What would you like to talk about?"

    return jsonify({'response': response})  # Send response back as JSON

if __name__ == '__main__':
    app.run(debug=True)

