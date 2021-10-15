FROM automation-runner:v1.0

RUN mkdir driver && mkdir tests

COPY /driver /driver

COPY /tests /tests

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT python3 tests/google_test.py
