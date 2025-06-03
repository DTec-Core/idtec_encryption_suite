
from idtec_core import signer
import os

def test_sign_file():
    sample_file = "sample.txt"

    assert os.path.exists(sample_file + ".idtec-signature")
