# SQL Formatter with LLM

## Overview

**SQL Formatter** is a web application built using  **Django**  and **DRF** that formats raw SQL queries into a neat, readable format using a **Language Learning Model (LLM)**. This project integrates the **Ollama3 8B model** for SQL formatting and supports both a web interface and REST API for SQL formatting.

---

## Features

- **Web Interface**: Users can input raw SQL queries and get a formatted version in a neat layout.
- **REST API**: Programmatic access to SQL formatting with a `POST` endpoint.
- **LLM Integration**: Uses **Ollama3 8B** for reformatting SQL queries.
- **Testing**: Unit and integration tests for validating functionality.
- **Dockerized**: Easy-to-setup environment with Docker.
- **Authorization**: Required User Auth via JWT tokens and Session cookies, which as well allows for Queries saved per user.

---

## Installation and Setup

**⚠️ This is a heavy Application, Ensure you have a decent machine with limited background applications running ⚠️**


### 1. Clone the repository:

HTTP:
```bash
git clone https://github.com/dhruvhooda/SQL_FORMATTER.git
cd SQL_FORMATTER
```

Be sure to do this in terminal(VsCode is best)

### 2. Install Docker (if not installed):

Follow the instructions at [Docker's official website](https://www.docker.com/get-started) to install Docker.

**DONT FORGET TO CREATE A USER AND INCREASE MEMORY LIMIT TO 8GB AND CPU LIMIT TO 8**

### 3. Build and Run with Docker:

This Application requires a bit of power due to its usage of a LLM, ensure your machine is clean and ready to go. If any errors occur, attempt to restart your machine and retry the application.

**If you are using Windows**

- Go to entrypoint.sh and change the End of Line Sequence to LF from CRLF, and save the file.

**If you are using Mac or intialized the SH file on your windows machine**

First make sure Docker Desktop is up and running.

```bash
docker-compose up
```

This will build the project, set up the containers, pull ollama, and start the application.

Be sure to wait until you see 🟢 Model pulled, you are now allowed to run the localhost 🟢, which means you can move on to Usage.

Once done with the application run
```bash
docker-compose down
```

and if you wish to clear the volumes (all the data stored within the application) include --volumes at the end of the command.

---

## Usage

### Web Interface:
- Be sure you are on your private web account.
- Visit http://localhost:8080/login.
- Login/Register your account
- You'll then be redirected to the SQL Formatter Page
- Paste your raw SQL query in the input form and click "Format SQL."
- Depending on your input, the LLM could take up to 1-2 minutes, but often should output within 30 seconds.
- You'll then be redirected to a results page
- Past formatted SQL queries will be displayed below the input form.
- To logout, go back to http://localhost:8080/login
---
## Managing Users

Create a superuser using

```bash
docker-compose run web python app/manage.py createsuperuser
```

And login using http://localhost:8080/admin/

there, you can manage all your users, including deletion.

---

## Documentation

### API Documentation:
- The project uses **Swagger** to document the REST API.
- Access the API docs at `http://localhost:8080/api/docs/` once the app is running.
- Here you can try a few APIs
   - User creation
   - User auth
   - Formatter Post
   - Formatter Get

---

## Testing

### Run Unit Tests:

```bash
docker-compose run web python app/manage.py test ___
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
   - **Ollama3 8B** is used to format SQL queries. It was preferred due to it's lack of need for an API key allowing for simplier setup process, and is placed in a function so mocking would be easier to impliment.

2. **User API**
   - Built using Djangos built in User authentication, allowing for simplicity and easy debugging.

3. **Formatter API**
   - Built using Djangos DRF toolkit, allowing for easier setup.

3. **Docker**:
   - The project is containerized using Docker to provide an easy-to-setup, consistent development environment. Docker Compose orchestrates the services.

4. **Testing**:
   - **Unit Tests**: Validates functionality of individual components like the User API and Formatter API.
   - **Integration Tests**: Ensures that all parts of the system work together correctly.

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
   - Enhance error handling for different failure scenarios.

3. **Performance Enhancements**:
   - Optimize communication between the Django app and Ollama for handling large queries and reducing latency.

4. **Custom SQL Formatting Settings**:
   - Allow users to configure how SQL queries should be formatted (e.g., line breaks, indentation style).

---

## Author

Built by **Dhruv (dhruv@galactica.gg)**.

---

## Resources

   - https://www.django-rest-framework.org/
   - https://docs.djangoproject.com/en/5.2/