FROM ubuntu:22.04

WORKDIR /app


RUN apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip

COPY requirements.txt .
COPY svm_model.pkl .
COPY fol /app/fol
COPY putty.exe .
COPY Check_V.py .

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt


CMD ["python3", "fol"]
CMD ["python3", "Check_V.py"]
