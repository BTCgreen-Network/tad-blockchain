import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("TAD_ROOT", "~/.tad/mainnet"))).resolve()
STANDALONE_ROOT_PATH = Path(
    os.path.expanduser(os.getenv("TAD_STANDALONE_WALLET_ROOT", "~/.tad/standalone_wallet"))
).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("TAD_KEYS_ROOT", "~/.tad_keys"))).resolve()
