# Use the official Manim Docker image as the base
FROM manimcommunity/manim:latest

# Switch to root to install additional packages
USER root

# Set the working directory
WORKDIR /manim

# Update package list and install any necessary system packages
RUN apt-get update && \
    apt-get install -y ffmpeg sox libsox-fmt-all xdg-utils && \
    rm -rf /var/lib/apt/lists/*

# Install manim-voiceover with desired extras
RUN pip install --upgrade "manim-voiceover[azure,gtts]"

# Optionally, switch back to a non-root user if required by the base image
# USER manim
