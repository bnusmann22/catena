FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (cached layer unless requirements change)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy application code
COPY . .

# Run as non-root for security
RUN adduser --disabled-password --no-create-home appuser
USER appuser

EXPOSE 5000

# Use gunicorn for production (4 workers, bind to all interfaces)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
