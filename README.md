

```markdown
# Greeting App

This is a simple Flask web application that displays a greeting message based on the user's input and the current time of day. The app uses Docker Compose to run both the Flask app and a Redis instance.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:

```
git clone https://github.com/your-username/greeting-app.git
```

2. Navigate to the project directory:

```
cd greeting-app
```

3. Build and start the containers:

```
docker-compose up --build
```

This command will build the Docker images and start the containers for the Flask app and Redis instance.

4. Once the containers are running, you can access the app at `http://localhost:5000`.

## Usage

1. Open the app in your web browser at `http://localhost:5000`.
2. Click the "Greet Me" button.
3. Enter your name when prompted.
4. The app will display a greeting message with your name and the current time of day (morning, afternoon, or evening).

## Technologies Used

- Python
- Flask
- Redis
- Docker
- Docker Compose

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```
