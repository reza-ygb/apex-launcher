# Use Python slim image for minimal size
FROM python:3.11-slim

# Install system dependencies for GUI support
RUN apt-get update && apt-get install -y \
    python3-pyqt5 \
    python3-pyqt5.qtquick \
    libqt5widgets5 \
    libqt5gui5 \
    libqt5core5a \
    libqt5dbus5 \
    libqt5network5 \
    libfontconfig1 \
    libxcb1 \
    python3-pil \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY apex_launcher.py .
COPY smart_cli_launcher.py .
COPY bin/apex-launcher ./bin/apex-launcher
COPY apex-launcher.png .
COPY VERSION .

# Make the launcher executable
RUN chmod +x ./bin/apex-launcher

# Set environment variables for GUI
ENV DISPLAY=:0
ENV QT_X11_NO_MITSHM=1
ENV XDG_RUNTIME_DIR=/tmp/runtime-root

# Create runtime directory
RUN mkdir -p /tmp/runtime-root && chmod 700 /tmp/runtime-root

# Add app to PATH
ENV PATH="/app/bin:${PATH}"

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 -c "import sys; sys.exit(0)"

# Default to CLI mode for better Docker compatibility
CMD ["apex-launcher", "--cli"]

# Metadata
LABEL maintainer="reza-ygb <https://github.com/reza-ygb>"
LABEL description="APEX Launcher - Ultimate Linux Application Launcher"
LABEL version="1.0.1"