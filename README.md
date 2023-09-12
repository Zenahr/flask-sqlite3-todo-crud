# flask-sqlite3-todo-crud with blackjack and prometheus

```console
docker compose -p otus-sre-hw15-p1 up
```

## Pipenv

```console
python -m pipenv install --python 3.11
python -m pipenv install flask==2.3.3 flask-sqlalchemy==3.1.1 gunicorn==21.2.0 prometheus-flask-exporter==0.22.4
```

## Dockerize

Build container:

```console
docker build -t flask-sqlite3-todo-crud .
```

Run container:

```console
docker run -d -p 9999:8080 --name flask-sqlite3-todo-crud flask-sqlite3-todo-crud
```
