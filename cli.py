
import click
from idtec_core import signer, threefish

@click.group()
def main():
    pass

@main.command()
@click.option('--file', required=True, help='File to sign')
@click.option('--key', required=True, help='Private key file')
def sign(file, key):
    signer.sign_file(file, key)

@main.command()
@click.option('--message', required=True, help='Message to encrypt')
@click.option('--key', required=True, help='256-bit key')
def encrypt(message, key):
    result = threefish.encrypt_message(message, key)
    click.echo(f"Encrypted: {result}")

if __name__ == '__main__':
    main()
