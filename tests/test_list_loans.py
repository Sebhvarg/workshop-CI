"""
Tests for Feature 4: List Loans
Owner: Issac Maza Punine - issamaza@espol.edu.ec
Branch: feature/list-loans
"""
import pytest
from unittest.mock import patch
from features.list_loans import list_loans

def test_list_loans_success(capsys):
    mock_data = {
        "books": {
            "101": {"title": "Book A", "author": "Author A"}
        },
        "members": {
            "M01": {"name": "Issac Maza"}
        },
        "loans": [
            {"book_id": "101", "member_id": "M01", "due_date": "2026-06-10"}
        ]
    }
    with patch("features.list_loans.load_data", return_value=mock_data):
        list_loans("M01")
        captured = capsys.readouterr()
        
        # Verify output mentions the member's name and the book details
        assert "Issac Maza" in captured.out
        assert "Book A" in captured.out
        assert "2026-06-10" in captured.out

def test_list_loans_no_loans(capsys):
    mock_data = {
        "books": {},
        "members": {
            "M01": {"name": "Issac Maza"}
        },
        "loans": []
    }
    with patch("features.list_loans.load_data", return_value=mock_data):
        list_loans("M01")
        captured = capsys.readouterr()
        
        # Verify output indicates no loans
        assert "no tiene libros en préstamo" in captured.out

def test_list_loans_member_not_found():
    mock_data = {
        "books": {},
        "members": {},
        "loans": []
    }
    with patch("features.list_loans.load_data", return_value=mock_data):
        with pytest.raises(ValueError, match="no está registrado"):
            list_loans("M01")
