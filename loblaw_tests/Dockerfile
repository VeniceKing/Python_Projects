FROM joyzoursky/python-chromedriver

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt
ENV PATH="usr/local/bin:${PATH}"

COPY . .

CMD [ "python3", "./tests.py" ]