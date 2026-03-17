# Agentic Design Patterns

**Agentic Design Patterns** are architectural and behavioral patterns for building autonomous AI agents and agentic
systems.

These patterns provide proven solutions for designing agents that can:

- **Perceive** their environment
- **Make decisions**
- **Take actions**
- **Iterate** toward achieving defined goals

They encompass various approaches including:

- **Reasoning frameworks**
- **Planning strategies**
- **Tool integration**
- **Memory management**
- **Multi-agent orchestration**

This enables developers to create intelligent systems that operate with minimal human intervention while maintaining
control and predictability.

## Getting Started

### Prerequisites

* Python 3.10 or higher is required.
* Provider API keys:
  - Anthropic (for Claude models)  
  - Google (for Gemini models)
  - OpenAI (for OpenAI models)

Library dependencies are listed in the `requirements.txt` file.

### Setup environment

1. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

2. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration API Keys

Provider API Keys are required to run the examples. You can put them in your shell configuration
file (e.g. `~/.zshrc` or `~/.bashrc`):

```bash
export ANTHROPIC_API_KEY="your-anthropic-api-key"
export GEMINI_API_KEY="your-gemini-api-key"
export OPENAI_API_KEY="your-openai-api-key"
```

## Available Patterns

### Chaining Pattern

Sequential task decomposition

* Anthropic implementation: [chaining/chaining_anthropic.py](chaining/chaining_anthropic.py)
* OpenAI implementation: [chaining/chaining_openai.py](chaining/chaining_openai.py)

### Routing Pattern

Intelligent request routing

* Google ADK implementation: [routing/routing_adk.py](routing/routing_adk.py)
