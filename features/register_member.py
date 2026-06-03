"""
Feature 1: Register a member, with a name and a unique identifier.
Owner: Eimmy Ochoa Morán - eimvocho@espol.edu.ec
Branch: feature/register-member
"""

from storage import load_data, save_data

def register_member(member_id: str, name: str) -> None:
    
    data = load_data()
    

    if member_id in data["members"]:
        raise ValueError(f"El miembro con ID '{member_id}' ya está registrado.")
    

    data["members"][member_id] = {"name": name}
    
    save_data(data)
    print(f"Miembro '{name}' registrado exitosamente con ID '{member_id}'.")