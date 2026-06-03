"""
Feature 1: Register a member, with a name and a unique identifier.
Owner: Eimmy Ochoa Morán - eimvocho@espol.edu.ec
Branch: feature/register-member
"""
from storage import load_data, save_data

def register_member(member_id: str, name: str) -> None:
    """
    Registers a new member with the library.
    """
    data = load_data()
    
    # Simplemente lo guardamos, sin validar si ya existe
    data["members"][member_id] = {"name": name}
    
    save_data(data)
    print(f"Miembro '{name}' registrado exitosamente con ID '{member_id}'.")