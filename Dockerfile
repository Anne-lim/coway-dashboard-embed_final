# Use the official Python image
FROM python:3.10-slim

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy your app code into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Streamlit configuration (needed for Cloud Run)
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8080
ENV STREAMLIT_SERVER_ENABLECORS=false

# Expose the port Streamlit will run on
EXPOSE 8080

# Command to run your Streamlit app
CMD ["streamlit", "run", "application.py", "--server.port=8080", "--server.address=0.0.0.0"]
