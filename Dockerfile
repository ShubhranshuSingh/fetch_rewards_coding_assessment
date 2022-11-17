FROM python:3.6.9-slim

WORKDIR fetch_rewards

COPY . ./
EXPOSE 5000

RUN pip3 install -r requirements.txt

CMD ["flask", "run"]