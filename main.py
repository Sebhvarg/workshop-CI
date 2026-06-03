import argparse
import sys
from features.register_member import register_member
from features.loan_book import loan_book
from features.return_book import return_book
from features.list_loans import list_loans
from features.report_overdue import report_overdue

def main():
    parser = argparse.ArgumentParser(description="CaféLibro — Library Loan Manager CLI")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Command to run")

    # Feature 1: Register Member
    register_parser = subparsers.add_parser("register-member", help="Register a new library member")
    register_parser.add_argument("--id", required=True, help="Unique member identifier")
    register_parser.add_argument("--name", required=True, help="Name of the member")

    # Feature 2: Loan Book
    loan_parser = subparsers.add_parser("loan-book", help="Loan a book to a member")
    loan_parser.add_argument("--book-id", required=True, help="Identifier of the book to loan")
    loan_parser.add_argument("--member-id", required=True, help="Identifier of the member")
    loan_parser.add_argument("--due-date", required=True, help="Due date for the loan (YYYY-MM-DD)")

    # Feature 3: Return Book
    return_parser = subparsers.add_parser("return-book", help="Return a book and mark it available")
    return_parser.add_argument("--book-id", required=True, help="Identifier of the book to return")

    # Feature 4: List Loans
    list_parser = subparsers.add_parser("list-loans", help="List books currently on loan to a member")
    list_parser.add_argument("--member-id", required=True, help="Identifier of the member")

    # Feature 5: Report Overdue
    overdue_parser = subparsers.add_parser("report-overdue", help="Report loans overdue relative to a reference date")
    overdue_parser.add_argument("--current-date", required=True, help="Reference date (YYYY-MM-DD)")

    args = parser.parse_args()

    try:
        if args.command == "register-member":
            register_member(args.id, args.name)
        elif args.command == "loan-book":
            loan_book(args.book_id, args.member_id, args.due_date)
        elif args.command == "return-book":
            return_book(args.book_id)
        elif args.command == "list-loans":
            list_loans(args.member_id)
        elif args.command == "report-overdue":
            report_overdue(args.current_date)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if _name_ == "_main_":
    main()