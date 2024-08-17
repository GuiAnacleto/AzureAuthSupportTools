import click

@click.group()
def cli():
    """Priority Support CLI."""
    pass

@cli.command()
@click.option('--name', default='User', help='Your name')
def greet(name):
    """Greet the user."""
    click.echo(f"Hello, {name}!")

@cli.command()
@click.option('--debug', is_flag=True, help='Enable debug mode')
def run(debug):
    """Run the CLI application."""
    if debug:
        click.echo("Debug mode is on.")
    else:
        click.echo("Running in normal mode.")

if __name__ == '__main__':
    cli()
