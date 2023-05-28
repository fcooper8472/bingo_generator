from .bingodata import BingoData


class BingoDoc:
    def __init__(self, bingo_data: BingoData):
        assert isinstance(bingo_data, BingoData), 'bingo_data must be an instance of BingoData'
        self.bingo_data = bingo_data

    def generate_doc(self):
        return True
