
import click
from idtec_core import signer, threefish

@main.command()
@click.option('--key', required=True, help='256-bit key')
def encrypt(message, key):
    result = threefish.encrypt_message(message, key)
    click.echo(f"Encrypted: {result}")

if __name__ == '__main__':
    main()
