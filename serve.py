"""Lightweight HTTP server to launch the Cyber-FinTech Audit Dashboard."""
import http.server
import os
import socketserver
import webbrowser

PORT = 8000
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


def start_server():
    print(f"\n=======================================================")
    print(f"🚀 Expense Auditor & Anomaly Hunter Dashboard Launching")
    print(f"🌐 Serving at: http://localhost:{PORT}")
    print(f"⚡ Press Ctrl+C to stop the server")
    print(f"=======================================================\n")
    webbrowser.open(f"http://localhost:{PORT}")
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")


if __name__ == "__main__":
    start_server()
