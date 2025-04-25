import click
from idtec_core.shake_hash import get_shake_hash
from idtec_core.lattice import generate_signature_keypair, sign_message, verify_signature

@click.command()
@click.option('--file', required=True, help='File to sign')
@click.option('--key', required=False, help='Optional key output')
def main(file, key):
    with open(file, "rb") as f:
        message = f.read()

    private_key, public_key = generate_signature_keypair()
    signature = sign_message(message, private_key)

    sig_file = file + ".idtec-signature"
    with open(sig_file, "wb") as sig:
        sig.write(signature)

    key_file = file + ".idtec-pubkey"
    with open(key_file, "wb") as kf:
        kf.write(public_key)

    print(f"[✔] Signature written to: {sig_file}")
    print(f"[✔] Public key written to: {key_file}")
