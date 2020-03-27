from pathlib import Path
import pickle


def load_index(indexfile=None):
    if indexfile is None:
        indexfile = Path(__file__).parent / "index.p"

    indexfile = Path(indexfile)
    with indexfile.open('rb') as index:
        return pickle.load(index)
