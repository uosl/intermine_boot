import click

@click.command()
@click.argument('mode')
@click.argument('target')
@click.option('--ci', is_flag=True, default=False, help='Run in CI mode.')
@click.option('--build-im', is_flag=True, default=False, help='Perform a build of InterMine prior to building the instance.')
@click.option('--im-repo', help='Build InterMine from this Git repository.')
@click.option('--im-branch', help='Use this branch when building InterMine.')
def cli(mode, target, ci, build_im, im_repo, im_branch):
    """Here will be a description of this script.
    Remember to also document modes and targets.

    MODE: [start | load | build | setup]

    TARGET: [local]
    """
    click.echo('Hello, World!')