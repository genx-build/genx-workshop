# Get started

setup env and install langchain

```bash
$ python3 -m venv .venv
‌$ pip install -r requirements.txt
```

for lint and work with jupyter notebook

```bash
‌$ pip install -r requirements_dev.txt
```

## langchain

it is a cool abstraction! that help create prototype of complex application fast.

it can connect LLM to external sources easily

### component

The core element of any language model application is the model.

- Prompts:

    a set of instructions or input provided by a user to guide the model's response

- Language models
- Output parsers

![model-io](./images/model_io.jpeg)

## Run server

in development

```bash
$ uvicorn src.main:app  --reload
INFO:     Will watch for changes in these directories: ['<path>']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [pid] using StatReload
INFO:     Started server process [pid]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
