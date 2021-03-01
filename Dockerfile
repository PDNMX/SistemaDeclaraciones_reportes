# Set base image (host OS)
FROM python:3.8

# Set the working directory in the container
WORKDIR /code

ARG NODE_ENV

# Copy the dependencies file to improve cache hints
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy all the files
COPY . .

EXPOSE 3001

# Command to run on container start
CMD [ "python", "./flask_app.py"]
