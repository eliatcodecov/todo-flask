# TODO Flask

A todo list app built with Flask. It uses Flask and Docker to stand up a simple todo list app.

## Building the app

```bash
docker build -t todo-app:latest .
```

## Running the app

```bash
docker run -p 8080:8080 todo-app:latest
```

## Accessing the app

Once running the app will be available at http://localhost:8080.
