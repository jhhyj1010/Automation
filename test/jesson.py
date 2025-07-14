#!/usr/bin/env python3

import click

@click.command()
@click.option("--count", default=1, help='Number of integar')
def hello(count):
    print("number is :",count)

if __name__ == '__main__':
    hello()
