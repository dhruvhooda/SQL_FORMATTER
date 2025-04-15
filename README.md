# SQL Formatter with LLM

## 🧠 Overview

**SQL Formatter** is a web application built using **Django** that formats raw SQL queries into a neat, readable format using a **Language Learning Model (LLM)**. This project integrates the **Ollama3 8B model** for SQL formatting and supports both a web interface and REST API for SQL formatting.

---

## 🚀 Features

- **Web Interface**: Users can input raw SQL queries and get a formatted version in a neat layout.
- **REST API**: Programmatic access to SQL formatting with a `POST` endpoint.
- **LLM Integration**: Uses **Ollama3 8B** for reformatting SQL queries.
- **Testing**: Unit and integration tests for validating functionality.
- **Dockerized**: Easy-to-setup environment with Docker.

---

## 🔧 Installation and Setup

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/sql-formatter-llm.git
cd sql-formatter-llm
```

### 2. Install Docker (if not installed):

Follow the instructions at [Docker's official website](https://www.docker.com/get-started) to install Docker and Docker Compose.

### 3. Setup Environment Variables:

Create a `.env` file in the root directory with the following environment variable:

```env
OLLAMA_API_URL=http://host.docker.internal:11434/api/generate
```

Ensure that you have the **Ollama3 8B** model pulled and running locally. You can do this by running:

```bash
ollama run ollama3
```

### 4. Build and Run with Docker:

```bash
docker-compose up --build
```

This will build the project, set up the containers, and start the application. By default:
- The **web interface** will be available at `http://localhost:8000/`
- The **API endpoint** can be accessed at `http://localhost:8000/api/format-sql/`

---

## 🧑‍💻 Usage

### Web Interface:
- Visit `http://localhost:8000/`.
- Paste your raw SQL query in the input form and click "Format SQL."
- The formatted SQL will be displayed below the input form.

### REST API:
You can interact with the SQL formatter programmatically via the REST API.

**Endpoint:**
```
POST /api/format-sql/
```

**Request:**
```json
{
  "query": "SELECT * FROM users WHERE age > 21"
}
```

**Response:**
```json
{
  "formatted_sql": "SELECT *\nFROM users\nWHERE age > 21;"
}
```

Swagger documentation for the API is available at `/api/docs/` (if enabled).

---

## 🧪 Testing

### Run Unit Tests:

```bash
docker-compose exec web python manage.py test
```

This will run the tests and give you a report on the test outcomes.

### Test Coverage:
- **LLM Service Tests**: Ensure that the LLM service correctly handles prompt generation and response formatting.
- **API Tests**: Verify that the API endpoint processes raw SQL and returns properly formatted SQL.
- **Web Interface Tests**: Ensure that form submissions return the expected results.

---

## 🧑‍💻 Design Choices and Implementation Details

### Core Components

1. **LLM Integration**:
   - We use **Ollama3 8B** to process SQL queries. A dedicated service module (`services/llm_formatter.py`) handles communication with the Ollama API. This module crafts a prompt, sends it to Ollama, and processes the response.

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

## 🛠️ Future Improvements

1. **User Authentication**:
   - Implement a user authentication system to allow users to save their formatted SQL queries.

2. **History Page**:
   - Add a feature to store the history of formatted queries in the database, allowing users to review past submissions.

3. **Advanced Error Handling**:
   - Enhance error handling for different failure scenarios, including invalid SQL queries or API issues.

4. **API Rate Limiting**:
   - Implement rate limiting for the API to prevent abuse.

5. **Pagination/CRUD for History**:
   - Add pagination and CRUD operations for managing saved SQL query history.

6. **Performance Enhancements**:
   - Optimize communication between the Django app and Ollama for handling large queries and reducing latency.

7. **Better SQL Formatting Rules**:
   - Improve the LLM prompt to generate even more readable SQL formats based on community-established best practices.

8. **Custom SQL Formatting Settings**:
   - Allow users to configure how SQL queries should be formatted (e.g., line breaks, indentation style).

---

## 📚 Documentation

### API Documentation:
- The project uses **Django Rest Framework's built-in documentation tools** (or **Swagger**) to document the REST API.
- Access the API docs at `http://localhost:8000/api/docs/` once the app is running.

---

## 🧑‍💻 Author

Built by **Dhruv**.
Feel free to open issues or make contributions!

---

## 📄 License

This project is licensed under the MIT License.

---

This template ensures that the **installation**, **usage**, **testing**, and **design** of your project are clearly outlined, providing a solid foundation for future development and contributions. You can expand it as you add more features or encounter changes in your project.