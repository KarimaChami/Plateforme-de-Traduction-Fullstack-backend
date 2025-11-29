# Étape 1 : Build stage
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


#Le premier ./app → chemin dans ton projet local (la source)/Le deuxième ./app → chemin dans le conteneur Docker (la destination).
COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0" , "--port", "8000"]