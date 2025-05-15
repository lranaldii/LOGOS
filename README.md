# LOGOS

**LOGOS** is a modular, template-driven prompt framework for building structured reasoning pipelines over large language models.

## Features

- **Pluggable modules**: each reasoning step is an isolated class loading its own template  
- **Easy configuration**: define module order and activation via `config.yaml`  
- **Plugin discovery**: support for external modules via entry-points (`logos_framework.modules`)  
- **LLM-agnostic client**: abstract interface, out-of-the-box OpenAI implementation  
- **Logging**: trace each module execution with timestamps and levels  
- **CLI**: simple command-line interface to run pipelines  
- **Testing ready**: designed for pytest and easy unit testing

---

## Installation

```bash
pip install logos-framework


```python
from prompt_framework.orchestrator import PipelineBuilder, Orchestrator
from prompt_framework.client import OpenAIClient

builder = PipelineBuilder("config.yaml")
modules = builder.load_modules()
client = OpenAIClient(api_key="YOUR_KEY")
orc = Orchestrator(modules=modules, client=client)

results = orc.execute("Complex problem....…")
print(results["explanation"])
```
