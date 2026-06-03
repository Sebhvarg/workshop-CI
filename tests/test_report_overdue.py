import pytest
from unittest.mock import patch
from features.report_overdue import report_overdue

def get_base_mock_data():
    return {
        "books": {
            "101": {"title": "Book A", "author": "Author A"},
            "102": {"title": "Book B", "author": "Author B"}
        },
        "members": {
            "M01": {"name": "Leonardo"}
        },
        "loans": [
            {"book_id": "101", "member_id": "M01", "due_date": "2026-06-01"}, # Overdue if checked on 2026-06-03
            {"book_id": "102", "member_id": "M01", "due_date": "2026-06-10"}  # Not overdue
        ]
    }

def test_report_overdue_found(capsys):
    mock_data = get_base_mock_data()
    with patch("features.report_overdue.load_data", return_value=mock_data):
        report_overdue("2026-06-03")
        captured = capsys.readouterr()
        
        # Should include book 101 but NOT book 102
        assert "Book A" in captured.out
        assert "2026-06-01" in captured.out
        assert "Book B" not in captured.out

def test_report_overdue_none_found(capsys):
    mock_data = get_base_mock_data()
    with patch("features.report_overdue.load_data", return_value=mock_data):
        report_overdue("2026-05-30") # Checked before all due dates
        captured = capsys.readouterr()
        
        assert "No se encontraron préstamos vencidos" in captured.out
        assert "Book A" not in captured.out
