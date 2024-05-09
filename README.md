# ix-promptfoo

This repository contains examples of [promptfoo](https://promptfoo.dev). To run this, promptfoo, Python >= 3.9 and the Python framework [langchain](https://python.langchain.com/v0.1/docs/get_started/introduction/) must be installed. To use OpenAI's GPT-3.5_turbo, you need a valid API key. Please export the key into your environment for example with

```
export OPENAI_API_KEY=sg......
```

To use local models from [Ollama](https://ollama.com), you need to install Ollama and its [models](https://ollama.com/library) first.

### Install promotfoo

On the command-line you can install promptfoo with

```
$ npm install -g promptfoo
```

or, if you would like to use npx

```
$ npx promptfoo@latest
```

### Install Python virtual environment

If you allready have Python installed, please add a virtual environment like

```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

### Install langchain

To install the necessary libraries run

```
$ pip install -r requirements.txt
```

on your command-line. 

### Run promptfoo examples

To run the different promptfoo examples use

```
$ npx promptfoo eval -c <promptfooconfig_XXX>.yaml
```

For example

```
$ npx promptfoo eval -c promptfooconfig_all_any.yaml
```

### View results

Promptfoo shows the result of a test run on the command line. To display the results in the browser you can use

```
$ npx promptfoo view
```

which starts the integrated server and displays the results in the web browser.

### Clean promptfoo cache

If nothing else is set, promptfoo uses a cache to avoid executing the same prompts multiple times against the providers (LLMs, scripts, etc.). To clear this cache just enter

```
$ npx promptfoo npx promptfoo clean cache
```

### Test RAG

To run the RAG evaluation ```promptfooconfig_rag.yaml``` you need to initialize a Chroma vector database with the content of [twenty-thousand-leagues-under-the-sea.txt](https://www.gutenberg.org/cache/epub/164/pg164.txt) from project Gutenberg. Therefor the ```insert_vdb.py``` script is implemented. If you would like to save some cents yo can use the existing vector database with all embeddings.

### Test Hugging Face classifiers

The promptfoo example ```promptfooconfig_classifier.yaml``` is using the [text classifiers from Hugging Face](https://huggingface.co/docs/transformers/tasks/sequence_classification). To use this, you need to export a valid Hugging Face API token like

```
$ export HF_API_TOKEN=.....
```