#!/usr/bin/env python3
import click

print("Jesson")
@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@cli.command()  # @cli, not @click!
def sync_hui():
    print("In sync command")
    click.echo('Syncing')

@cli.command()
def sync_jesson():
    click.echo('syncing jesson')

def main():
    cli(prog_name='jesson')

if __name__ == '__main__':
    main()

