import tempfile

from bingogen.bingodata import BingoData
from bingogen.bingodoc import BingoDoc


def test_bingo_doc_init():

    with tempfile.NamedTemporaryFile() as temp:
        bd = BingoData(temp.name)

        bd_doc = BingoDoc(bd)
