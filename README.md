# HOw to run (Windows)
```sh
docker run -it --rm -v ${PWD}:/app -w /app python:3.13-slim bash
```

```sh
source ./venv/bin/activate
pip install -r requirements.txt
python grid.py
```

Note: Currently dockerfile not being used

# Adjusting grid
- edit width, height, spacing in the python file