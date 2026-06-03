"""
Feature 4: List the books a member currently has on loan.
Owner: Issac Maza Punine - issamaza@espol.edu.ec
Branch: feature/list-loans
"""
from storage import load_data

def list_loans(member_id: str) -> None:
    """
    Lists the books a specific member currently has on loan.
    """
    data = load_data()
    
    # Validate member existence
    if member_id not in data["members"]:
        raise ValueError(f"El miembro con ID '{member_id}' no está registrado.")
        
    # Get active loans
    member_loans = [loan for loan in data["loans"] if loan["member_id"] == member_id]
    
    if not member_loans:
        print(f"El miembro con ID '{member_id}' no tiene libros en préstamo actualmente.")
        return
        
    print(f"Libros en préstamo para el miembro '{data['members'][member_id]['name']}' ({member_id}):")
    for loan in member_loans:
        book_id = loan["book_id"]
        book_info = data["books"].get(book_id, {"title": "Desconocido", "author": "Desconocido"})
        print(f" - [{book_id}] {book_info['title']} por {book_info['author']} (Vence: {loan['due_date']})")
