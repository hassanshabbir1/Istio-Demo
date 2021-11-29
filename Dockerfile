FROM python:3.8 

WORKDIR ./

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip install Flask
RUN pip install dash
RUN pip install dash-bootstrap-components
RUN pip install requests


COPY ./ ./

CMD ["python", "./front_end.py"]
