FROM alpine:latest


COPY * /app/

WORKDIR /app

RUN apk update && apk add bash && apk add python3
RUN apk add make && apk add pip3


RUN make install
CMD ["echo", "Welcome to my csv to json image!"]
