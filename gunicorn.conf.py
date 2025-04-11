import multiprocessing

# Gunicorn configuration file
# https://docs.gunicorn.org/en/latest/configure.html

# Server socket
bind = "0.0.0.0:$PORT"  # Render sets PORT environment variable
workers = multiprocessing.cpu_count() * 2 + 1  # Recommended formula

# Timeouts
timeout = 120  # Increased timeout for model loading and predictions
keepalive = 5

# Server mechanics
preload_app = True  # Load application before worker processes are forked
worker_class = 'sync'  # Standard synchronous workers

# Logging
accesslog = '-'  # Log to stdout
errorlog = '-'   # Log to stdout
loglevel = 'info'