FROM python:3.10-bullseye
LABEL maintainer="Abdou Nasser abdounasser202@gmail.com"
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--reload", "--host", "0.0.0.0", "--port", "5000"]
