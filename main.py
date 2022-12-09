import click
from main_class import CreateServer


@click.group()
def main():
    pass


@main.group()
def create():
    pass


@create.command("node-server")
@click.option("--path", "-p", type=str, prompt="path", required=True, help="Enter the absolute path where you want to create the server")
def create_node(path):
    mongo_uri = click.prompt("MongoDB URI :", type=str)
    click.confirm("Do you want to continue with this Mongo Uri", abort=True)
    click.echo(path)
    click.echo(mongo_uri)
    create_server = CreateServer(path)
    create_server.build()

    if mongo_uri != "":
        create_server.create_dotenv(mongo_uri)


if __name__ == "__main__":
    main()
