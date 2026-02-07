#!/usr/bin/env python3
"""
Simple Flask server for MammaSabe website
Includes keep-alive mechanism to prevent Render from sleeping
"""

from flask import Flask, send_from_directory, send_file
import threading
import time
import requests
import os

app = Flask(__name__, static_folder='.')

# Get the port from environment variable (Render provides this)
PORT = int(os.environ.get('PORT', 8080))

# Your Render URL (will be set after first deploy)
RENDER_URL = os.environ.get('RENDER_URL', '')

@app.route('/')
def index():
    """Serve the main index.html"""
    return send_file('index.html')

@app.route('/health')
def health():
    """Health check endpoint for Render and keep-alive pings"""
    return {'status': 'ok', 'message': 'MammaSabe is alive!'}, 200

@app.route('/<path:path>')
def serve_static(path):
    """Serve all other static files"""
    try:
        return send_from_directory('.', path)
    except:
        return send_file('index.html')  # Fallback to index for SPAs

def keep_alive():
    """
    Keep-alive function that pings the server every 14 minutes
    to prevent Render free tier from sleeping after 15 minutes
    """
    if not RENDER_URL:
        print("⚠️  RENDER_URL not set. Keep-alive disabled.")
        return
    
    while True:
        try:
            time.sleep(14 * 60)  # Wait 14 minutes
            response = requests.get(f"{RENDER_URL}/health", timeout=10)
            if response.status_code == 200:
                print("✅ Keep-alive ping successful")
            else:
                print(f"⚠️  Keep-alive ping returned status {response.status_code}")
        except Exception as e:
            print(f"❌ Keep-alive ping failed: {e}")

if __name__ == '__main__':
    # Start keep-alive thread if RENDER_URL is set
    if RENDER_URL:
        keep_alive_thread = threading.Thread(target=keep_alive, daemon=True)
        keep_alive_thread.start()
        print(f"🔄 Keep-alive mechanism started for {RENDER_URL}")
    
    print(f"🚀 Starting MammaSabe server on port {PORT}")
    print(f"📁 Serving files from: {os.getcwd()}")
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=PORT, debug=False)
