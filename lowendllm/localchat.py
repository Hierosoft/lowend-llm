import os
import sys
from logging import getLogger

import ollama

from lowendllm import ollama_model_name

logger = getLogger(__name__)

def main():
    if len(sys.argv) < 2:
        logger.error("You must specify a file or text.")
        return 1
    if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as stream:
            user_input = stream.read()
    else:
        if len(sys.argv) == 2:
            logger.warning(
                "You only provided one word, but it is not a file."
                " Assuming it was what you wanted to ask...")
        user_input = " ".join(sys.argv[1:])

    stream = ollama.chat(
        model='deepseek-r1',
        messages=[{'role': 'user', 'content': user_input}],
        stream=True
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        # generated_response += chunk['message']['content']
    return 1

# if __name__ == "__main__":
#     sys.exit(main())