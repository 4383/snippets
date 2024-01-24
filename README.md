# Snippets

Backup of my code snippets, PoC, and tests.

## Python

See the [Python directory](python/).

Launch an appropriated an environment:

```bash
$ git clone https://github.com/4383/machine
$ docker build -t machine-python310 .
$ docker run -it --rm --name mpython310 --mount type=bind,source="$(pwd)",target=/home/developer/app machine-python310 /bin/bash
> python3.10 app/python/asyncio.py
```
