import json
import numpy as np
import cv2
from io import BytesIO
import gzip

def loadMapData(file_path):
    # Loads and returns Core Keeper map data
    # as a JSON object
    with gzip.open(file_path, 'rt') as f:
        data = json.load(f)
    return data    

def completeImage(json_data):
    # Builds image from grid of pngs from Core Keeper
    # map data

    # Args:
    #   json_data: mapparts file from Core Keeper converted to JSON

    keys = json_data['mapParts']['keys']
    values = json_data['mapParts']['values']

    # Find the minimum and maximum x and y coordinates
    min_x = min(key['x'] for key in keys)
    max_x = max(key['x'] for key in keys)
    min_y = min(key['y'] for key in keys)
    max_y = max(key['y'] for key in keys)

    # Calculate the width and height of the complete image
    image_width = (max_x - min_x + 1) * 256
    image_height = (max_y - min_y + 1) * 256

    # Create an empty image (black background)
    complete_image = np.zeros((image_height, image_width, 4), dtype=np.uint8)

    # Iterate through the image tiles and place them in the complete image
    for i, key in enumerate(keys):
        x = key['x'] + abs(min_x)
        y = max_y - key['y']

        # Decode the PNG data from the 'values' array
        image_stream = BytesIO(bytes(values[i]['png']))
        tile_image = cv2.imdecode(np.frombuffer(image_stream.read(), np.uint8), cv2.IMREAD_UNCHANGED)

        # Place the tile image in the complete image
        complete_image[y * 256:(y + 1) * 256, x * 256:(x + 1) * 256] = tile_image

    return complete_image