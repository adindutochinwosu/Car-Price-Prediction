# provide a base/python image pulled from Docker Hub
FROM python:3.8 

# create working directory , called app, in the docker container
CMD mkdir /usr/app1

# change Docker's cwd to the created directory
WORKDIR /usr/app1

# install all the dependencies and required libraries
# for a rebuild only run the requirements.txt if
# the content changes
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# expose this port to run the application
# port 8501 is a convention used by various tools as the default
EXPOSE 8501

# copy all files from cwd on my laptop to the Docker container's cwd
COPY . /usr/app1/

# specify how thw docker container will run
ENTRYPOINT ["streamlit", "run"]

# specify which application the docker should run
CMD ["app.py"]

