# Water jugs riddle implementation

Implementation of the water jugs riddle with dynamic inputs using python/django and docker

# Building the project

docker build -f Dockerfile -t docker-django-v0.0:latest .

# Running the project

docker run -it --env-file ./.env -p 8000:8000 docker-django-v0.0
