import click
from cli_flows.connection_setup_flow import ConnectionSetupFlow
from cli_flows.connection_view_flow import ConnectionViewFlow
from cli_flows.group_create_flow import GroupCreateFlow
from cli_flows.group_edit_flow import GroupEditFlow
from cli_flows.group_view_flow import GroupViewFlow


@click.group()
def glt():
    """Welcome to gitlab-tools!"""


@click.option('-s', '--setup', is_flag=True, help='Setup connection settings')
@click.option('-v', '--view', is_flag=True, help='View connection settings')
@glt.command()
def connection(setup: bool, view: bool):
    """Setup or view gitlab connection settings"""

    if not check_flags([setup, view]):
        return

    if setup:
        ConnectionSetupFlow().start()
    elif view:
        ConnectionViewFlow.start()


@click.option('-c', '--create', is_flag=True, help='Create a new group of repositories to work with')
@click.option('-e', '--edit', is_flag=True, help='Edit an existing group of repositories')
@click.option('-v', '--view', is_flag=True, help='View existing groups with their contents')
@glt.command()
def groups(create: bool, edit: bool, view: bool):
    """Working with groups of repositories"""

    if not check_flags([create, edit, view]):
        return

    if create:

        GroupCreateFlow().start_create_group_flow()
    elif edit:
        GroupEditFlow().start_edit_group_flow()
    elif view:
        GroupViewFlow().start_view_groups_flow()

    return


def check_flags(args_list):
    args = tuple(args_list)
    specified_flags_count = sum(args)

    if specified_flags_count != 1:
        print('You need to specify one option for the command (just one).')
        return False
    else:
        return True
