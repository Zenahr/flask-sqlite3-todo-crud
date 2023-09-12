# flask-sqlite3-todo-crud with blackjack and prometheus

## Dockerize

Build container:

```console
docker build -t flask-sqlite3-todo-crud .
```

Run container:

```console
docker run -d -p 9999:8080 --name flask-sqlite3-todo-crud flask-sqlite3-todo-crud
```