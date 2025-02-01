import http.server
import socketserver
import os
import sys

def start_server():
    # Define the port to run the server on
    PORT = 8080

    # Set the directory where your HTML file is located
    WEB_DIR = os.path.dirname(os.path.abspath(__file__))  # The current directory

    # Create the handler to serve files from the directory
    Handler = http.server.SimpleHTTPRequestHandler

    # Change the working directory to the one where your index.html is located
    os.chdir(WEB_DIR)

    try:
        # Start the HTTP server on port 8080
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving at port {PORT}...")
            httpd.serve_forever()
        return 0  # Server ran successfully
    except Exception as e:
        print(f"Error: {e}")
        return 1  # Return non-zero code in case of error


def main():
    return start_server()


if __name__ == "__main__":
    sys.exit(main())  # Run the main function and exit with the returned status code
