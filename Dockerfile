# Use an official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything from your local folder into the Docker image
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default Streamlit port
EXPOSE 8501

# Run your Streamlit app
CMD ["streamlit", "run", "app.py"]
