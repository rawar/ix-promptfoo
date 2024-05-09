# ix-promptfoo

This repository contains examples of [promptfoo](https://promptfoo.dev). To run this, promptfoo, Python >= 3.9 and the Python framework [langchain](https://python.langchain.com/v0.1/docs/get_started/introduction/) must be installed.

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