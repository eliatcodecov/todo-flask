build:
	docker build -t todo-app:latest .

run:
	docker run -p 8080:8080 todo-app:latest

