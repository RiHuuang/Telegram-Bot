from flask import Flask, request, jsonify
from telegram import Bot
import asyncio

# Initialize Flask app and Telegram bot
app = Flask(__name__)
TELEGRAM_BOT_TOKEN = '7953043239:AAEgxpg6ulY7RTwYUyU9MQj7f3Bduxul7_Q'
CHAT_ID = '-1002302233939'  # Replace with the chat ID or group ID where you want to send the message
bot = Bot(token=TELEGRAM_BOT_TOKEN)

@app.route('/api/hit', methods=['POST'])
def api_hit():
    """
    Endpoint to handle API hits.
    Sends a message to the Telegram bot when this endpoint is hit.
    """
    data = request.json  # Receive JSON data from the request
    message = data.get("message", "An API hit was received!")  # Default message
    
    try:
        # Use asyncio to call the coroutine
        asyncio.run(bot.send_message(chat_id=CHAT_ID, text=message))
        return jsonify({"success": True, "message": "Message sent to Telegram."}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
