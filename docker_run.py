#!/usr/bin/env python3
"""
This script runs the docker command locally to allow
for ingest of notebook file and output of markdown.
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import subprocess
from subprocess import PIPE, STDOUT


def main(args):
    """ Run this docker command

    docker run -e INPUT=tests/resources/blog_test-hugo_blog.ipynb -e OUTPUT=./ --rm --volume $(pwd):/home --name temp_nb2hugo nb2hugo
    """
    bashCommand = [f"""docker run \
                                -e INPUT={args.input} \
                                -e OUTPUT={args.output} \
                                --rm \
                                --volume $(pwd):/home \
                                --name temp_nb2hugo \
                                nb2hugo 
                                """]
    subprocess.call(bashCommand, shell=True)
    return 1
   


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("input", help="input .ipynb notebook file")
    parser.add_argument("output", help="output markdown file")
    args = parser.parse_args()
    main(args)