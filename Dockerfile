FROM python:3.13-slim

# Install dependencies for Pillow
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
 && rm -rf /var/lib/apt/lists/*

# Install Pillow
RUN pip install --no-cache-dir Pillow

# Set work directory
WORKDIR /app

# Copy your script here (optional)
COPY grid.py .

CMD ["python3 grid.py"]
