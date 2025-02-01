import requests
import json
import sys

# See <https://medium.com/@nitinsgavane/2025-guide-run-deepseek-r1-locally-with-ollama-in-10-minutes-build-your-own-ai-web-recon-tool-0816335bc48d>

SELF_HELP_INPUT = """
Why isn't this Unpoly request using post correctly? The server says POST is not accepted, but "Post" works fine when using Python or PowerShell. The powershell that works fine is `Invoke-WebRequest -Uri "http://localhost:5000/generate" -Method Post -ContentType "application/json" -Body $body`. Try to make the JavaScript Unpoly request work:
const response = await up.request('http://localhost:5000/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ input: userInput })
            });
"""
SELF_HELP_INPUT = None  # turn off self-help


def main():
    # Define the URL
    url = "http://localhost:5000/generate"

    # Define the headers
    headers = {
        "Content-Type": "application/json"
    }

    if len(sys.argv) < 2 and not SELF_HELP_INPUT:
        print("Specify an LLM query.")
        return 1

    if not SELF_HELP_INPUT:
        req_s = ""
        for arg in sys.argv[1:]:
            req_s += " " + arg
    else:
        req_s = SELF_HELP_INPUT

    req_s = req_s.strip()

    # Define the data
    data = {
        "input": "{}".format(req_s)
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check the response status code
    if response.status_code == 200:
        print(response.content)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
