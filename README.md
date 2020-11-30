### build

```
docker build -t schose/logtest:latest .
```

### test

```
docker run --rm -e LOOPS=30 schose/logtest:latest
```

### push to docker hub

```
docker push schose/logtest:latest
```