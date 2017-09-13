FROM heroku/heroku:16

RUN apt-get update
RUN apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8
RUN apt-get install -y python-pip python-mecab

ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
ADD . /opt/webapp/
WORKDIR /opt/webapp
