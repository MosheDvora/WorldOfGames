FROM python:3.7.5-slim
ADD . /WorldOfGames
WORKDIR /WorldOfGames
RUN pip install  -r requirements.txt
CMD ["python", "MainScores.py"]
