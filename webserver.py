import http.server
import socketserver
import time
import os
import imageHandling
import cv2

PORT = 8000  # Choose a port for your web server
gzipPath = 'server-map-gzip/0.mapparts.gzip'

class WebHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'  # Serve the HTML file

        # Update the map image every 60 seconds
        if time.time() - os.path.getmtime('generated_images/map.png') > 60:
            file_path = gzipPath
            json_data = imageHandling.loadMapData(file_path)
            full_image = imageHandling.completeImage(json_data)
            cv2.imwrite('generated_images/map.png', full_image)

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = WebHandler

# Generate the initial map image
file_path = gzipPath
json_data = imageHandling.loadMapData(file_path)
full_image = imageHandling.completeImage(json_data)
cv2.imwrite('generated_images/map.png', full_image)

# Start the web server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()