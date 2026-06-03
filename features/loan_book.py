from storage import load_data, save_data

def loan_book(book_id: str, member_id: str, due_date: str) -> None:

    data = load_data()
    
    if book_id not in data["books"]:
        raise ValueError(f"El libro con ID '{book_id}' no existe en el catálogo.")
    
    if member_id not in data["members"]:
        raise ValueError(f"El miembro con ID '{member_id}' no está registrado.")
    
    for loan in data["loans"]:
        if loan["book_id"] == book_id:
            raise ValueError(f"El libro con ID '{book_id}' ya se encuentra prestado.")
            
    member_loans_count = sum(1 for loan in data["loans"] if loan["member_id"] == member_id)
    if member_loans_count >= 3:
        raise ValueError(f"El miembro con ID '{member_id}' ya tiene el límite de 3 libros prestados.")
    
    data["loans"].append({
        "book_id": book_id,
        "member_id": member_id,
        "due_date": due_date
    })
    
    save_data(data)
    print(f"Libro '{book_id}' prestado exitosamente al miembro '{member_id}' hasta {due_date}.")