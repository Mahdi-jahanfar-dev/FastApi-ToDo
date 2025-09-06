# choosing python version
FROM python:3.12

# setting work directory
WORKDIR /core

# copying requirements file
COPY ./requirements.txt /core/requirements.txt

# installing dependencies
RUN pip install --no-cache-dir --upgrade -r /core/requirements.txt

# copying project files
COPY . /core/

