FROM python:3.12

WORKDIR /usr/src/app
#COPY ./poetry.lock /usr/src/app
#COPY ./pyproject.toml /usr/src/app
COPY . /usr/src/app
RUN pip install --no-cache-dir poetry
RUN poetry install


CMD [ "python", "manage.py", "runserver" ]
