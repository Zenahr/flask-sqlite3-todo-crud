FROM python:3.8

RUN pip install pipenv

ENV PROJECT_DIR /app

COPY . /${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}

RUN pipenv install --system --deploy

CMD ["gunicorn", "--graceful-timeout", "5", "--chdir", ".", "app:app",  "-w", "4", "-b", "0.0.0.0:8080"]