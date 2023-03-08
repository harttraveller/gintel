import click


@click.group()
def entry():
    pass


@entry.group()
def configure():
    pass


@configure.command()
def tokens():
    pass
