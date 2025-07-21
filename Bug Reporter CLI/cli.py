import argparse
from bugs.manager import add_bug, update_bug, delete_bug, load_bugs, print_bugs

parser = argparse.ArgumentParser(description="Bug Reporter CLI")
subparsers = parser.add_subparsers(dest="command")

# -------- Add Bug --------
add_parser = subparsers.add_parser("add", help="Add a new bug")
add_parser.add_argument("--title", required=True, help="Bug title")
add_parser.add_argument("--description", required=True, help="Bug description")
add_parser.add_argument("--priority", default="low", help="Bug priority")
add_parser.add_argument("--status", default="open", help="Bug status")
add_parser.add_argument("--assigned-to", dest="assigned_to", help="Assignee name")

# -------- Update Bug --------
update_parser = subparsers.add_parser("update", help="Update a bug")
update_parser.add_argument("id", help="Bug ID")
update_parser.add_argument("--title")
update_parser.add_argument("--description")
update_parser.add_argument("--priority")
update_parser.add_argument("--status")
update_parser.add_argument("--assigned-to", dest="assigned_to")

# -------- Delete Bug --------
delete_parser = subparsers.add_parser("delete", help="Delete a bug")
delete_parser.add_argument("id", help="Bug ID")

# -------- List Bugs --------
parser_list = subparsers.add_parser("list", help="List all bugs")
parser_list.add_argument("--status", help="Filter by status")
parser_list.add_argument("--priority", help="Filter by priority")

# -------- Search Bugs --------
search_parser = subparsers.add_parser("search", help="Search bugs by title or description")
search_parser.add_argument("query", help="Search query")

args = parser.parse_args()

# -------- Handle Commands --------
if args.command == "add":
    bug = add_bug(
        args.title,
        args.description,
        args.priority,
        assigned_to=args.assigned_to
    )
    print(f"Bug added with ID: {bug.id}")

elif args.command == "update":
    try:
        updated = update_bug(
            args.id,
            title=args.title,
            description=args.description,
            priority=args.priority,
            status=args.status,
            assigned_to=args.assigned_to
        )
        if updated:
            print(f"Bug updated: {updated.to_dict()}")
        else:
            print("Bug not found.")
    except Exception as e:
        print(f"Error updating bug: {e}")
        print_bugs()

elif args.command == "delete":
    try:
        deleted = delete_bug(args.id)
        if deleted:
            print(f"Bug deleted: {deleted.to_dict()}")
        else:
            print("Bug not found.")
    except Exception as e:
        print(f"Error deleting bug: {e}")
        print_bugs()

elif args.command == "list":
    from bugs.manager import list_bugs
    bugs = list_bugs(status=args.status, priority=args.priority)
    if not bugs:
        print("No bugs found.")
    else:
        print("\nAvailable Bugs:")
        for bug in bugs:
            print(f"  [{bug.id}] {bug.title} - Priority: {bug.priority}, Status: {bug.status}")

elif args.command == "search":
    from bugs.manager import search_bugs
    bugs = search_bugs(args.query)
    if not bugs:
        print("No bugs found.")
    else:
        print("\nAvailable Bugs:")
        for bug in bugs:
            print(f"  [{bug.id}] {bug.title} - Priority: {bug.priority}, Status: {bug.status}")
else:
    print("Invalid command. Use 'add', 'update', 'delete', or 'list'.")