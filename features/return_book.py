from storage import load_data, save_data

def return_book(book_id: str) -> None:

    data = load_data()
    
    loan_to_remove = None
    for loan in data["loans"]:
        if loan["book_id"] == book_id:
            loan_to_remove = loan
            break
            
    if loan_to_remove is None:
        raise ValueError(f"El libro con ID '{book_id}' no está prestado actualmente.")
           
    data["loans"].remove(loan_to_remove)
    
    save_data(data)
    print(f"Libro '{book_id}' devuelto exitosamente. Ahora está disponible.")