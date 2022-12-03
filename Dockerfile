FROM python:3.8-slim-buster
WORKDIR /bms
COPY requirement.txt requirements.txt
RUN python3 -m venv env
RUN source env/bin/activate
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "manage.py" ,"runserver", "--host=0.0.0.0"]
