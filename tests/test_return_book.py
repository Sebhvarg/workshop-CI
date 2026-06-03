import pytest
from unittest.mock import patch
from features.return_book import return_book

def test_return_book_success():
    mock_data = {
        "books": {
            "101": {"title": "Book A", "author": "Author A"}
        },
        "members": {
            "M01": {"name": "Sebastian"}
        },
        "loans": [
            {"book_id": "101", "member_id": "M01", "due_date": "2026-03-06"}
        ]
    }
    with patch("features.return_book.load_data", return_value=mock_data), \
         patch("features.return_book.save_data") as mock_save:
        
        return_book("101")
        
        assert len(mock_data["loans"]) == 0
        mock_save.assert_called_once_with(mock_data)
