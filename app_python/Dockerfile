FROM python

COPY . /app_python
WORKDIR /app_python

RUN adduser local && chown -R local /app_python
USER local

RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]