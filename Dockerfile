FROM alpine:3.6
#RUN apk add --no-cache nodejs-current
RUN apk add --no-cache python3
RUN apk add --no-cache gcc python3-dev linux-headers musl-dev libffi-dev openssl-dev

WORKDIR /opt/anagrams
ENV PYTHONPATH=/opt/anagrams
COPY requirements.txt requirments.txt
RUN easy_install-3.6 pip
#RUN pip install -r requirements.txt
RUN pip install flask gunicorn


COPY templates templates/
COPY static static/
COPY words.txt words.txt
COPY sowpods.txt sowpods.txt
COPY application.py application.py
COPY anagrams.py anagrams.py
COPY gunicorn.config gunicorn.config
copy entrypoint.sh entrypoint.sh
RUN chmod a+x entrypoint.sh
EXPOSE 8000
CMD ["/bin/sh", "-c", "/opt/anagrams/entrypoint.sh"]
