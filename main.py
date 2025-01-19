import argparse
import json
import logging
import pathlib

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger()

from ollama import chat
from ollama import ChatResponse


def get_parser():
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Prompt ollama with a collection of images",
    )
    parser.add_argument(
        "-s",
        "--streaming",
        action="store_true",
        help="print each inference result as it is produced, instead of all results at the end. (default: %(default)s)",
    )
    parser.add_argument(
        "-m",
        "--model",
        default="moondream",
        help="the ollama vision model to use (default: %(default)s)\nsee 'https://ollama.com/search?c=vision' for compatible models.",
    )
    parser.add_argument("prompt")
    parser.add_argument(
        "image",
        type=pathlib.Path,
        default=[],
        nargs="*",
    )
    return parser


def ask(query: str, image: pathlib.Path, model="llama3.2-vision"):
    messages = [{"role": "user", "content": query, "images": [image]}]

    response: ChatResponse = chat(model, messages)
    return response.message.content


def process_images(model, prompt, images):
    for i in images:
        llm_result = ask(prompt, image=i, model=model)
        result = {"image": str(i), "response": llm_result}
        yield (result)


def main(streaming=False):
    parser = get_parser()
    args = parser.parse_args()
    result_stream = process_images(args.model, args.prompt, args.image)
    if args.streaming:
        for result in result_stream:
            print(json.dumps(result))
    else:
        print(json.dumps(list(result_stream)))


if __name__ == "__main__":
    main()
