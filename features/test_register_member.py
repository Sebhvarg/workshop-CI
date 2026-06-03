"""
Tests for Feature 1: Register Member
Owner: Eimmy Ochoa Morán - eimvocho@espol.edu.ec
Branch: feature/register-member
"""
import pytest
from unittest.mock import patch
from features.register_member import register_member

def test_register_member_success():
    mock_data = {
        "books": {},
        "members": {},
        "loans": []
    }
    with patch("features.register_member.load_data", return_value=mock_data), \
         patch("features.register_member.save_data") as mock_save:
        
        register_member("M01", "Eimmy Ochoa")
        
        # Assert member was added to dictionary
        assert "M01" in mock_data["members"]
        assert mock_data["members"]["M01"]["name"] == "Eimmy Ochoa"
        mock_save.assert_called_once_with(mock_data)