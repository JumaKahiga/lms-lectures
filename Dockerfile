FROM python:3.7

MAINTAINER Kenneth Kabiru "kabirumwangi@gmail.com"

WORKDIR /app

# copy the file containing the app dependencies
COPY ./requirements.txt ./

# install all the dependencies
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["sh"]

CMD ["entry_point.sh"]