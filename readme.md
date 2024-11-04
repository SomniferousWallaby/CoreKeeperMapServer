# CoreKeeperMapImageLoader
This project provides a tool for generating and displaying a complete map image from the individual map tile data found in a Core Keeper save file.

## Features:

* Reads map tile data from a Core Keeper save file (typically 0.mapparts.gzip).
* Stitches individual map tiles together based on their coordinates to create a complete map image.

* Can be run as a standalone python webserver or deployed as a Docker container.

## Requirements:

* Python 3.10 or higher
* OpenCV (opencv-python)
* Requests (requests)
* NumPy (numpy)

## Usage:

1. Install Dependencies:

```pip install -r requirements.txt```

2. Run the script
```python webserver.py```


## Docker Deployment:

1. Build the Docker Image:

```docker build -t corekeeper-map-server .```

2. Run the Docker Container:

```docker run -d -p 8000:8000 corekeeper-map-server```
* Access the map webpage at http://localhost:8000/ (or your server's IP address if running remotely).

## Configuration:

* The script reads map data from a file named 0.mapparts.gzip by default. You can change this in the `webserver.py` script.
* The tile width and height are set to 256x256 pixels by default. Adjust these values in imageHandling.py if necessary.

## License:

This project is licensed under the MIT License.

## Acknowledgments:

Thanks to the developers of OpenCV, Requests, and NumPy for their excellent libraries.