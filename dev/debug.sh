docker-compose run --rm -p 5000:5000 -p 5678:5678 app python -m debugpy --listen 0.0.0.0:5678 --wait-for-client flask run --reload --host 0.0.0.0 --port 5000
