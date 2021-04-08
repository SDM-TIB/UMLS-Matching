FROM ubuntu:18.04

WORKDIR /umlsmatching
ADD . /umlsmatching

RUN apt-get --assume-yes update
RUN apt-get --assume-yes install python3 python3-flask python3-pip

RUN pip3 install elasticsearch

# Make port 5000 available to the world outside this container
EXPOSE 5000


# Run app.py when the container launches
CMD python3 ./api.py

