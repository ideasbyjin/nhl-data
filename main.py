#!/usr/bin/env python

"""
Get data from the NHL stats API.
"""
from nhlservice.const import CURRENT
from nhlservice.service import *
from utils.io import write

import click, sys

@click.group()
def cli():
    pass

@cli.command()
@click.option("--id", help = "Specify an id for the team. e.g. 8471214")
@click.option("--season",
              default = CURRENT,
              help = "Specify a season for getting stats.")
@click.argument("outfile", default = "out.jsonl")
def get_player_list(id: str, season: str, outfile: str):
    """
    Get the list of players for every team. Can specify a team ID and season.
    """

    player_list = query_player_list(id, season)
    write(player_list, outfile)

@cli.command()
@click.option("--id", help = "Specify an id for the player. e.g. 8471214")
@click.option("--season",
              default = CURRENT,
              help = "Specify a season for getting stats.")
@click.argument("outfile", default = "out.jsonl")
def get_player_stats(id: str, season: str, outfile: str):
    """
    Get a player's game log in JSON per line format.
    """
    if id is None:
        bail(get_player_stats)

    player_stats = query_player(id, season)
    write(player_stats, outfile)


def bail(command):
    with click.Context(command) as ctx:
        click.echo(command.get_help(ctx))
        sys.exit(0)

if __name__ == "__main__":
    cli()