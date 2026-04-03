from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CloudService(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)
        if parsed_url.path == "/":
            self.show_form()
        elif parsed_url.path == "/process":
            self.process_request(params)
    
    def show_form(self):
        html = """
        <html>
        <body>
            <h2>Cloud Computing Simulation</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>
                Enter number of users:
                <input type="number" name="users"><br><br>
                <input type="submit" value="Send Request">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())
    
    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        users = int(params.get("users", [1])[0])
        if users <= 100:
            response = "Low Load"
        elif users <= 500:
            response = "Medium Load"
        elif users > 500:
            response = "High Load!! Scaling Needed!"
        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>Users accessing service: {users}</p>
            <p>System Status: <b>{response}</b></p>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())
server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Cloud service running on port 8000...")
server.serve_forever()
