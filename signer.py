import click
from idtec_core.shake_hash import get_shake_hash

@click.command()
@click.option('--file', required=True, help='File to sign')
def main(file, key):
    with open(file, "rb") as f:
        message = f.read()

    print(f"[✔] Signature written to: {sig_file}")
    print(f"[✔] Public key written to: {key_file}")
