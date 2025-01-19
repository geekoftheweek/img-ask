```
usage: main.py [-h] [-s] [-m MODEL] prompt [image ...]

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
