FROM ubuntu:22.04

WORKDIR /app

COPY requirements.txt .
COPY svm_model.pkl .
COPY Check_V.py .

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/bin/python3:${PATH}"

RUN if [ -f svm_model.pkl ]; then echo "File exists!"; else echo "File does not exist!"; fi

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

CMD ["python", "Check_V.py"]

