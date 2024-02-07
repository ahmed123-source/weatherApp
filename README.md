# Weather App

This is a simple web application built with Flask that retrieves weather information for a given city using the OpenWeatherMap API.

## Features

- Allows users to input a city and retrieve its current weather information.
- Dockerized for easy deployment.

## Prerequisites

- Python 3 installed on your system.
- Docker (optional, for running the application in a container).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/weather-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd weather-app
    ```

3. Set up a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the application in your browser at `http://localhost:5000`.

3. Enter a city in the input field and click "Get Weather" to retrieve weather information.

## Docker Usage

1. Build the Docker image:

    ```bash
    docker build -t my-flask-app .
    ```

2. Run a container based on the image:

    ```bash
    docker run -p 5000:5000 my-flask-app
    ```

3. Access the application in your browser at `http://localhost:5000`.

