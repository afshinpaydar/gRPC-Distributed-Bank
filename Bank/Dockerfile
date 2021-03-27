FROM python:3.9-slim-buster
WORKDIR /app
EXPOSE 50054 50055 50056 50057 50058
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY src/ .
#ENTRYPOINT [ "python", "Branch.py", "input.json"]
CMD [ "python", "Branch.py", "input.json"]
