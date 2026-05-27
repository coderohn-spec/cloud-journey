# Cloud Journey Week 2

## Docker Projects

### weather-api
Python script that fetches live weather using requests library.
Packaged as Docker image.

To run:
docker build -t weather-api:1.0 .
docker run -it weather-api:1.0

### file-organizer
Python script that scans a folder and sorts files by type automatically.
Packaged as Docker image.

To run:
docker build -f Dockerfile.day6 -t file-organizer:1.0 .
docker run -it file-organizer:1.0

### Progress
- Day 1: Docker fundamentals, containers, images, SSH
- Day 2: Created Dockerfile, built weather-api image
- Day 3: Created Dockerfile.day6, built file-organizer image