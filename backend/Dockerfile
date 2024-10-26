# Use the official Manim Docker image as the base
FROM manimcommunity/manim:latest

# Set the working directory
WORKDIR /manim

# Install manim-voiceover
RUN pip install --upgrade "manim-voiceover[azure,gtts]"

RUN pip install --upgrade "manim-voiceover"


USER root
RUN apt-get update