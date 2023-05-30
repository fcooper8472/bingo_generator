import pathlib
import pytest

from bingogen.bingodata import BingoData

from utils import get_data_dir


def test_bingo_data_init():

    data_file_path = get_data_dir() / 'five_items_no_empty_line.txt'
    bd = BingoData(data_file_path)
    assert bd._file_path == pathlib.Path(data_file_path)


def test_bingo_data_init_invalid_path():
    # This path should not exist
    invalid_file_path = '/path/to/invalid/file'

    with pytest.raises(FileNotFoundError) as error:
        BingoData(invalid_file_path)

    assert 'invalid' in str(error.value)
    assert 'file does not exist' in str(error.value)


def test_bingo_data_five_items_no_empty_line():

    data_file_path = get_data_dir() / 'five_items_no_empty_line.txt'
    bingo_data = BingoData(data_file_path)

    assert bingo_data.num_data_items == 5
    assert bingo_data.data[0] == 'Item 1'
    assert bingo_data.data[4] == 'Item 5'


def test_bingo_data_five_items_with_empty_line():

    data_file_path = get_data_dir() / 'five_items_with_empty_line.txt'
    bingo_data = BingoData(data_file_path)

    assert bingo_data.num_data_items == 5
    assert bingo_data.data[2] == 'Item 3'
    assert bingo_data.data[3] == 'Item 4'


def test_bingo_data_no_items():

    data_file_path = get_data_dir() / 'no_items.txt'

    with pytest.raises(ValueError) as error:
        BingoData(data_file_path)

    assert 'no data found in' in str(error.value)


def test_long_lines():

    data_file_path = get_data_dir() / 'long_lines.txt'

    with pytest.warns(UserWarning) as record_of_warnings:
        BingoData(data_file_path)

    assert len(record_of_warnings) == 2

    for warning in record_of_warnings:
        assert 'is longer than 50 characters and might not format nicely' in str(warning.message)


def test_sample_too_big():

    data_file_path = get_data_dir() / 'five_items_with_empty_line.txt'
    bingo_data = BingoData(data_file_path)

    with pytest.raises(ValueError) as error:
        bingo_data.get_random_n(7)

    assert 'requested a sample of size 7, but there are only 5 entries' in str(error.value)


def test_longer_input():

    data_file_path = get_data_dir() / 'longer_input.txt'

    bingo_data = BingoData(data_file_path)
    assert bingo_data.num_data_items == 34

    list_of_8 = bingo_data.get_random_n(8)
    assert len(list_of_8) == 8
    for item in list_of_8:
        assert item in bingo_data.data

    list_of_22 = bingo_data.get_random_n(22)
    assert len(list_of_22) == 22
    for item in list_of_22:
        assert item in bingo_data.data
