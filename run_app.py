import http.server
import socketserver
import webbrowser
import threading
import time
import sys
import os

# Configuration
PORT = 8000
FILE_NAME = "ohpyne.html"

# Ensure we are serving the correct directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def start_server():
    # Quietly handle requests to avoid cluttering the window
    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            pass

    try:
        with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
            print(f"✅ Local Server running at http://localhost:{PORT}")
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 98 or e.errno == 10048: # Port already in use
            print(f"⚠️ Port {PORT} is busy. The app might already be running.")
        else:
            print(f"❌ Error starting server: {e}")

# Run server in a background thread
thread = threading.Thread(target=start_server)
thread.daemon = True
thread.start()

print("🚀 Launching OhPyne...")
time.sleep(1) # Give server a moment to spin up

# Open the browser
webbrowser.open(f'http://localhost:{PORT}/{FILE_NAME}')

print("\n---------------------------------------------------")
print("  APP IS RUNNING. DO NOT CLOSE THIS WINDOW.")
print("  To stop the app, simply close this window.")
print("---------------------------------------------------")

# Keep the window open
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...")
    sys.exit()