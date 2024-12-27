# LLM Web Parser

A Python-based tool that combines web scraping and AI-powered summarization to generate concise, markdown-formatted summaries of web content.

## Features

- Web scraping using BeautifulSoup4
- Content cleaning and preprocessing
- AI-powered summarization using OpenAI's GPT models / Local Ollama models
- Markdown-formatted output
- Jupyter notebook implementation

## Prerequisites

- Python 3.11+
- OpenAI API key
- Required Python packages:
  - requests
  - beautifulsoup4
  - python-dotenv
  - openai
  - IPython
  - ollama

## Setup

1. Clone this repository
2. Create a conda env using `conda env create -f environment.yml`.
3. Activate the env using `conda activate llms`.
4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## Usage

The main functionality is implemented in `web_parser.ipynb`. The notebook provides two main functions:

- `summarize(url, llm)`: Returns a markdown-formatted summary of the webpage using the specified LLM ("openai" or "ollama")
- `display_summary(url, llm)`: Displays the formatted summary in a Jupyter notebook

Example usage:
```python
# Get summary as string
## Using OpenAI
summary = summarize("https://example.com", "openai")
display_summary("https://example.com", "openai")

## Using Ollama
summary = summarize("https://example.com", "ollama")
display_summary("https://example.com", "ollama")
```

## How It Works

1. The `Website` class handles web scraping:
   - Fetches webpage content using requests
   - Removes irrelevant elements (scripts, styles, images)
   - Extracts clean text content using BeautifulSoup

2. The summarization process:
   - Supoorts two LLM backends
     - OpenAI's GPT models via API
     - Local Ollama models (default: llama3.2)
   - Formats output in markdown
   - Preserves important structural elements of the content

