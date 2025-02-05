FROM python:latest

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.2.1/zsh-in-docker.sh)"

WORKDIR /app

CMD ["zsh"]