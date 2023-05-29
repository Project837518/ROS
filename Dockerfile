FROM Ubuntu

WORKDIR /app

COPY requirements.txt .
COPY svm_model.pkl .
COPY Check_V.py .


RUN if [ -f svm_model.pkl ]; then echo "File exists!"; else echo "File does not exist!"; fi
RUN stat -c %s requirements.txt


CMD ["python", "Check_V.py"]

