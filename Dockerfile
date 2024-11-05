# Use a slim Python base image
FROM python:3.12.4-slim 

# Set the working directory inside the container
WORKDIR /app 

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxext6 \
    libxrender1 \
    libgtk2.0-0

RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY webserver.py /app/
COPY imageHandling.py /app/
COPY server-map-gzip/0.mapparts.gzip /app/server-map-gzip/
COPY index.html /app/

# Create a directory for generated images
RUN mkdir generated_images

# Expose the web server port
EXPOSE 8000

# Set the entrypoint command to run your web server
CMD ["python", "webserver.py"] 
