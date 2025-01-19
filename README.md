# img-ask

## Installation

### With uv

```
uv run img-ask -h
```

### With pip

```
python -m venv .venv
source .venv/bin/activate
pip install .
img-ask -h
```

### Troubleshooting

If you don't end up with a runnable `img-ask` command on your path, first make sure your virtual environment is activated.

If all else fails, you can always `pip install ollama` and then `python main.py -h`.

## Usage

```
usage: img-ask [-h] [-s] [-m MODEL] prompt [image ...]

Prompt ollama with a collection of images

positional arguments:
  prompt
  image

options:
  -h, --help            show this help message and exit
  -s, --streaming       print each inference result as it is produced, instead
                        of all results at the end. (default: False)
  -m MODEL, --model MODEL
                        the ollama vision model to use (default: moondream)
                        see 'https://ollama.com/search?c=vision' for
                        compatible models.
```
