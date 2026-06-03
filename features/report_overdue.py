
from storage import load_data

def report_overdue(current_date: str) -> None:
    """
    Reports all loans that are overdue relative to the given current_date.
    """
    data = load_data()
    
    overdue_loans = []
    for loan in data["loans"]:
        if loan["due_date"] < current_date:
            overdue_loans.append(loan)
            
    if not overdue_loans:
        print(f"No se encontraron préstamos vencidos para la fecha {current_date}.")
        return
        
    print(f"⚠️ PRÉSTAMOS VENCIDOS a la fecha {current_date}:")
    for loan in overdue_loans:
        book_id = loan["book_id"]
        member_id = loan["member_id"]
        
        book_info = data["books"].get(book_id, {"title": "Desconocido", "author": "Desconocido"})
        member_info = data["members"].get(member_id, {"name": "Desconocido"})
        
        print(f" - Libro: [{book_id}] '{book_info['title']}' | Prestado a: [{member_id}] {member_info['name']} | Venció: {loan['due_date']}")
