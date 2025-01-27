# FastAPI Docker Template

A production-ready FastAPI template configured for Docker deployment. This template is designed to help you quickly set up a robust and scalable FastAPI application with Docker.

## Features

- 🚀 **FastAPI with async support**: Leverage the power of asynchronous programming to handle many requests efficiently.
- 🐳 **Docker optimized**: Easily build and deploy your application using Docker, ensuring consistency across different environments.
- 🔐 **CORS middleware configured**: Secure your API by configuring Cross-Origin Resource Sharing (CORS) to control which domains can access your resources.
- 🏥 **Health check endpoint**: Monitor the health of your application with a built-in health check endpoint.
- 📚 **Auto-generated API documentation**: Automatically generate interactive API documentation using Swagger UI and ReDoc.

## Project Structure

- `Dockerfile`: Contains the instructions to build the Docker image, including setting up the environment, installing dependencies, and defining the command to run the application.
- `.gitignore`: Specifies files and directories to be ignored by git, such as Python cache files, virtual environments, and IDE-specific files.
- `requirements.txt`: Lists the dependencies required by the application, which are installed using pip.
- `app/`: Contains the FastAPI application code, including the main application file, routers, models, and any other necessary modules.
- `README.md`: Provides an overview and documentation of the project, including features, project structure, and setup instructions.