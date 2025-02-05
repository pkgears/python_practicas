## Build

docker build -t python_zsh .

## Run

```zsh
docker run -v $(pwd):/app --name python-test -it python_zsh
docker start -ia python-test
```
