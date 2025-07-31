import argparse
from bugs.manager import add_bug, update_bug, delete_bug, list_bugs, search_bugs, add_comment, update_status

def create_parser():
    """Create and return the command-line argument parser."""
    parser = argparse.ArgumentParser(description="Bug Reporter CLI")
    subparsers = parser.add_subparsers(dest="command")

    # -------- Add Bug --------
    add_parser = subparsers.add_parser("add", help="Add a new bug")
    add_parser.add_argument("--title", required=True, help="Bug title")
    add_parser.add_argument("--description", required=True, help="Bug description")
    add_parser.add_argument("--priority", default="low", help="Bug priority")
    add_parser.add_argument("--status", default="open", help="Bug status")
    add_parser.add_argument("--assigned-to", dest="assigned_to", help="Assignee name")
    add_parser.add_argument("--tags", nargs='*', default=[], help="Tags for the bug")

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

    # -------- Comments --------
    comment_parser = subparsers.add_parser("comment", help="Add a comment to a bug")
    comment_parser.add_argument("bug_id", help="Bug ID")
    comment_parser.add_argument("comment", help="Comment content")

    # -------- Update Status --------
    status_parser = subparsers.add_parser("status", help="Update bug status")
    status_parser.add_argument("bug_id", help="Bug ID")
    status_parser.add_argument("to", help="New status")

    return parser

def handle_args(args):
    """Handle parsed CLI arguments."""
    try:
        if args.command == "add":
            bug = add_bug(args.title, args.description, args.priority, args.assigned_to, args.tags)
            print(f"Bug added with ID: {bug.id}")

        elif args.command == "update":
            updated = update_bug(args.id, args.title, args.description, args.priority, args.status, args.assigned_to)
            if updated:
                print(f"Bug updated: {updated.to_dict()}")
            else:
                print("Bug not found.")

        elif args.command == "delete":
            deleted = delete_bug(args.id)
            if deleted:
                print("Bug deleted successfully.")
            else:
                print("Bug not found.")

        elif args.command == "list":
            bugs = list_bugs(status=args.status, priority=args.priority)
            if not bugs:
                print("No bugs found.")
            else:
                for bug in bugs:
                    print(f"[{bug.id}] {bug.title} - Priority: {bug.priority}, Status: {bug.status}")

        elif args.command == "search":
            bugs = search_bugs(args.query)
            if not bugs:
                print("No bugs found.")
            else:
                for bug in bugs:
                    print(f"[{bug.id}] {bug.title} - Priority: {bug.priority}, Status: {bug.status}")

        elif args.command == "comment":
            bug = add_comment(args.bug_id, args.comment)
            print(f"Comment added to bug {args.bug_id}: {bug.comments[-1]}")

        elif args.command == "status":
            bug = update_status(args.bug_id, args.to)
            print(f"Bug {args.bug_id} status updated to '{args.to}'")

        else:
            print("Invalid command. Use 'add', 'update', 'delete', 'list', 'status', or 'search'.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    handle_args(args)
