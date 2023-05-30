from bingogen.bingodata import BingoData
from bingogen.bingodoc import BingoDoc

from utils import get_data_dir


def test_bingo_doc_init():

    # Create BingoData object
    data_file_path = get_data_dir() / 'five_items_no_empty_line.txt'
    bd = BingoData(data_file_path)

    # Create BingoDoc object
    bingo_doc = BingoDoc(bd)
    assert bingo_doc.generate_doc()
