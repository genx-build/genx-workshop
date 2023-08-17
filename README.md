# Get started

setup env and install langchain

```bash
$ python3 -m venv .venv
‌$ pip install langchain
```

## langchain

it is a cool abstraction! that help create prototype of complex application fast.

it can connect LLM to external sources easily

### component

The core element of any language model application is the model.

- Prompts: a set of instructions or input provided by a user to guide the model's response
- LLMs: Large language models like GPT-3, BLOOM, etc
- Agents: Agents use LLMs to decide what actions should be taken. Tools like web search or calculators can be used,    and all are packaged into a logical loop of operations.
- Output parsers

![model-io](./images/model_io.jpeg)
