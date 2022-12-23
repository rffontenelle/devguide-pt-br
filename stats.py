#!/usr/bin/python3

import os
import argparse
import subprocess

DEFAULT_TEXT = "Translation Stats\n=================\n\n.. code-block::"

def create_parse() -> argparse.Namespace:
    current_dir = os.getcwd()
    parser = argparse.ArgumentParser("Outputs a reStructuredText-formatted page "
                                     "with translation statistics of po files.")
    parser.add_argument("--text", "-t", default=DEFAULT_TEXT,
                        help="Custom text preceeding the statistics (title, introductions, etc.)")
    parser.add_argument("--podir", "-p", default=current_dir,
                        help="Path containing the PO files; "
                             f"defaults to the current directory ({current_dir})")
    parser.add_argument("--file", "-f", default=None,
                        help="Store output to this file")
    return parser.parse_args()


def stats(po_dir: str, output_file: str, begin_text=DEFAULT_TEXT) -> str:
    """Run ``potodo`` using *po_dir* as argument, and return its output
    in a formatted text. If running potodo fails, return None
    """
    formatted_text = ''
    try:
        todo_text = subprocess.run(
            ['potodo', '-p', args.podir], encoding="UTF-8", check=True,
            stdout=subprocess.PIPE).stdout.replace('\n', '\n    ')
        formatted_text = f"{begin_text}{todo_text}"
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        print(f"An error occurred when running 'potodo': {error}")
    
    return formatted_text


if __name__ == "__main__":
    args = create_parse()
    stats_text = stats(args.podir, args.file)
    if stats_text:
        if args.file:
            with open(args.file, "w") as file:
                file.write(stats_text)
        else:
            print(stats_text)
