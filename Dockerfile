FROM python:3.12


WORKDIR /core

COPY ./requirements.txt /core/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /core/requirements.txt


COPY . /core/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]