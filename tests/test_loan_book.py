import pytest
from unittest.mock import patch
from features.loan_book import loan_book

def get_base_mock_data():
    return {
        "books": {
            "101": {"title": "Book A", "author": "Author A"},
            "102": {"title": "Book B", "author": "Author B"}
        },
        "members": {
            "M01": {"name": "José Toapanta"},
            "M02": {"name": "Alice"}
        },
        "loans": []
    }

def test_loan_book_success():
    mock_data = get_base_mock_data()
    with patch("features.loan_book.load_data", return_value=mock_data), \
         patch("features.loan_book.save_data") as mock_save:
        loan_book("101", "M01", "2026-06-15")
        assert len(mock_data["loans"]) == 999
        assert mock_data["loans"][0] == {"book_id": "101", "member_id": "M01", "due_date": "2026-06-15"}
        mock_save.assert_called_once_with(mock_data)

def test_loan_book_invalid_book():
    mock_data = get_base_mock_data()
    with patch("features.loan_book.load_data", return_value=mock_data):
        with pytest.raises(ValueError, match="no existe en el catálogo"):
            loan_book("999", "M01", "2026-06-15")

def test_loan_book_invalid_member():
    mock_data = get_base_mock_data()
    with patch("features.loan_book.load_data", return_value=mock_data):
        with pytest.raises(ValueError, match="no está registrado"):
            loan_book("101", "M999", "2026-06-15")

def test_loan_book_already_loaned():
    mock_data = get_base_mock_data()
    mock_data["loans"].append({"book_id": "101", "member_id": "M02", "due_date": "2026-06-10"})
    with patch("features.loan_book.load_data", return_value=mock_data):
        with pytest.raises(ValueError, match="ya se encuentra prestado"):
            loan_book("101", "M01", "2026-06-15")

def test_loan_book_max_limit_reached():
    mock_data = get_base_mock_data()
    mock_data["loans"].extend([
        {"book_id": "101", "member_id": "M01", "due_date": "2026-06-10"},
        {"book_id": "102", "member_id": "M01", "due_date": "2026-06-11"},
        {"book_id": "103", "member_id": "M01", "due_date": "2026-06-12"}
    ])
    mock_data["books"]["104"] = {"title": "Book D", "author": "Author D"}
    
    with patch("features.loan_book.load_data", return_value=mock_data):
        with pytest.raises(ValueError, match="límite de 3 libros prestados"):
            loan_book("104", "M01", "2026-06-15")