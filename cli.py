import click
from gitlab_api.gitlab_adapter import GitlabAdapter
from gitlab_api.gitlab_adapter import Group
from cli_flows import connection_flow


@click.group()
def glt():
    """Welcome to gitlab-tools!"""


@click.option('-s', '--setup', is_flag=True, help='Setup connection settings')
@click.option('-v', '--view', is_flag=True, help='View connection settings')
@glt.command()
def connection(setup: bool, view: bool):
    """Setup or view gitlab connection settings"""
    args = (setup, view)
    specified_flags_count = sum(args)

    if specified_flags_count != 1:
        print('You need to specify one option for the command (just one).')
        return

    if setup:
        connection_flow.start_setup_connection_flow()
    elif view:
        connection_flow.start_view_connection_flow()
