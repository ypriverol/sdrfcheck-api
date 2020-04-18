import click
import connexion
from flask_cors import CORS


#
# _PUBLIC_REGISTRY_URL = "http://biocontainers.pro/registry/"
from encoder import JSONEncoder


def print_help(ctx, param, value):
    if value is False:
        return
    click.echo(ctx.get_help())
    ctx.exit()


@click.command()
@click.option('--help', is_flag=True, expose_value=False, is_eager=False, callback=print_help,
              help="Print help message")
@click.pass_context
def main(ctx,):
    app = connexion.App(__name__, specification_dir='./swagger/')
    CORS(app.app, expose_headers='next_page, last_page, self_link, current_offset, current_limit')  # adds CORS support
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'SDRF Restful API'})
    app.run(port=8090)

if __name__ == '__main__':
    main()
