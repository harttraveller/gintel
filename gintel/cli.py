import click


@click.group()
def entry():
    pass


@entry.group()
def tokens():
    pass


@tokens.command()
def view():
    pass


@tokens.command()
def add():
    pass


@tokens.command()
def delete():
    pass


@tokens.command()
def change():
    pass


@tokens.command()
def copy():
    pass
