# SQL Formatter with LLM

## Overview

**SQL Formatter** is a web application built using **Django** that formats raw SQL queries into a neat, readable format using a **Language Learning Model (LLM)**. This project integrates the **Ollama3 8B model** for SQL formatting and supports both a web interface and REST API for SQL formatting.

---

## Features

- **Web Interface**: Users can input raw SQL queries and get a formatted version in a neat layout.
- **REST API**: Programmatic access to SQL formatting with a `POST` endpoint.
- **LLM Integration**: Uses **Ollama3 8B** for reformatting SQL queries.
- **Testing**: Unit and integration tests for validating functionality.
- **Dockerized**: Easy-to-setup environment with Docker.
- **Authorization**: Required User Auth via JWT tokens which as well allows for Queries saved per user.

---

## Installation and Setup

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/sql-formatter-llm.git
cd SQL_formatter
```

### 2. Install Docker (if not installed):

Follow the instructions at [Docker's official website](https://www.docker.com/get-started) to install Docker.

### 3. Setup Environment Variables:

Ensure that you have the **Ollama3 8B** model pulled and running locally. You can do this by running:

```bash
ollama run ollama3
```

### 4. Build and Run with Docker:

```bash
docker-compose up
```

This will build the project, set up the containers, and start the application.

to Simply build the container use:

```bash
docker-compose build
```


---

## Usage

### Web Interface:
- Visit `http://localhost:8080/login`.
- Login/Register your account
- You'll then be redirected to the SQL Formatter Page
- Paste your raw SQL query in the input form and click "Format SQL."
- You'll then be redirected to a results page
- Past formatted SQL queries will be displayed below the input form.

---

## Documentation

### API Documentation:
- The project uses **Swagger** to document the REST API.
- Access the API docs at `http://localhost:8080/api/docs/` once the app is running.
- Here you can test a few APIs
   - User creation
   - User auth
   - Formatter Post
   - Formatter Get

---

## Testing

### Run Unit Tests:

```bash
docker-compose exec web python app/manage.py test ___
```

This will run the tests based off which application you are testing, replace the ___ with which application you wish to test.

### Application Tests:
- **user**: Ensures User creation and light error handling
- **formatter**: Ensures formatter input and can correctly format; light error handling


### Run Intergration Tests:

- Utilizes Github Actions for Intergration testing.
- Everytime code is pushed it automatically runs.

---

## Design Choices and Implementation Details

### Core Components

1. **LLM Integration**:
   - **Ollama3 8B** is used to format SQL queries. A dedicated service module (`services/llm_formatter.py`) handles communication with the Ollama API. This module crafts a prompt, sends it to Ollama, and processes the response.

2. **Django Views**:
   - A class-based view (`views.py`) handles both web form submissions and API requests. The view:
     - Accepts a raw SQL query from the user.
     - Passes it to the LLM service for formatting.
     - Returns the formatted SQL back to the user via the web interface or API.

3. **REST API**:
   - The REST API endpoint `/api/format-sql/` accepts a `POST` request with a raw SQL query and returns the formatted query.
   - The API is built using **Django Rest Framework** (DRF), providing easy serialization and documentation through Swagger.

4. **Docker**:
   - The project is containerized using Docker to provide an easy-to-setup, consistent development environment. Docker Compose orchestrates the services.

5. **Testing**:
   - **Unit Tests**: Validates functionality of individual components like the prompt generator and API responses.
   - **Integration Tests**: Ensures that all parts of the system (front-end, back-end, LLM integration) work together correctly.

### Key Technologies:
- **Django**: Framework for building the web application and REST API.
- **Ollama3 8B**: The LLM used for formatting SQL queries.
- **Django Rest Framework**: For building the API and handling serialization.
- **Docker**: For containerizing the application.

---

## Future Improvements

1. **History Page**:
   - Add a feature to store the history of formatted queries in the database, allowing users to review past submissions.

2. **Advanced Error Handling**:
   - Enhance error handling for different failure scenarios, including invalid SQL queries or API issues.

3. **API Rate Limiting**:
   - Implement rate limiting for the API to prevent abuse.

4. **Pagination/CRUD for History**:
   - Add pagination and CRUD operations for managing saved SQL query history.

5. **Performance Enhancements**:
   - Optimize communication between the Django app and Ollama for handling large queries and reducing latency.

6. **Better SQL Formatting Rules**:
   - Improve the LLM prompt to generate even more readable SQL formats based on community-established best practices.

7. **Custom SQL Formatting Settings**:
   - Allow users to configure how SQL queries should be formatted (e.g., line breaks, indentation style).

---

## Author

Built by **Dhruv (dhruv@galactica.gg)**.