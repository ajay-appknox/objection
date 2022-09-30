import os
import click
from objection.state.connection import state_connection


def disable(args: list = None) -> None:
    """
        Attempts to disable jailbreak detection.

        :param args:
        :return:
    """

    api = state_connection.get_api()
    api.ios_jailbreak_disable()
    
    
def custom(args: list = None) -> None:
    """
        Attempts to disable jailbreak detection using a custom list.

        :param args:
        :return:
    """
    
    if len(args) <= 0:
        click.secho('Usage: ios jailbreak custom <file_list>', bold=True)
        return
    else:
        click.secho("Attempting to disable jailbreak detection using custom list: {}".format(args[0]), bold=True)

    api = state_connection.get_api()
    
    if os.path.exists(args[0]):
        with open(args[0]) as f:
            _ = f.read().splitlines()
            api.ios_jailbreak_custom(_)
    else:
        click.secho("File doesn't exists: {}".format(args[0]), fg='red', bold=True)
        return


def simulate(args: list = None) -> None:
    """
        Attempts to simulate a Jailbroken environment

        :param args:
        :return:
    """

    api = state_connection.get_api()
    api.ios_jailbreak_enable()
