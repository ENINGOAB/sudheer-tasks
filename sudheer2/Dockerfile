FROM python:2.7-slim
WORKDIR /webserver
ADD . /webserver
RUN pip install --trusted-host pypi.python.org Flask
RUN pip install requests
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install --no-cache-dir dnspython
CMD ["python", "webserver.py"]
