FROM python:stretch

ADD app.py requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]