import pytest

from features.return_book import returnbook

def test_return_book_success(capsys):

    returnbook()

    captured = capsys.readouterr()
  
    assert captured.out == "Returning a book...\n"