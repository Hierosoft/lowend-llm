import ollama
import sys
import threading

from logging import getLogger
from flask import (
    Flask,
    jsonify,
    request,
)

from lowendllm.webfrontend import main as frontend_main  # Import main from frontend


logger = getLogger(__name__)
app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate_text():
    user_input = request.json.get('input')
    print("Got input '''{}''' in '''{}'''"
          .format(user_input, request.json))

    if not user_input:
        logger.error("No input provided.")
        return jsonify({"error": "No input provided"}), 400

    generated_response = ""

    stream = ollama.chat(
        model='deepseek-r1',  # Replace with the model you want to use
        messages=[{'role': 'user', 'content': user_input}],
        stream=True
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        generated_response += chunk['message']['content']

    print(
        "Returning generated text (length {}): {}"
        .format(len(generated_response),
                generated_response))
    return jsonify({"generated_text": generated_response})


def run_flask():
    app.run(debug=True, use_reloader=False, port=5000)  # Flask on port 5000


def run_frontend():
    frontend_main()  # Run frontend's main function


def main():
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    frontend_thread = threading.Thread(target=run_frontend, daemon=True)

    flask_thread.start()
    frontend_thread.start()

    flask_thread.join()
    frontend_thread.join()


if __name__ == "__main__":
    sys.exit(main())
