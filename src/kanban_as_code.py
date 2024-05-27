#!/usr/bin/env python3

import argparse


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="Kanban as Code - a hackable text-based Kanban board."
    )

    g = parser.add_mutually_exclusive_group()
    g.add_argument(
        "--create", "-c", action="store_true", help="Create a new blank Kanban board."
    )
    g.add_argument("--verify", "-v", action="store_true", help="Verify a Kanban board.")
    g.add_argument("--list", "-l", action="store_true", help="List a Kanban board.")
    parser.add_argument(
        "--file",
        "-f",
        type=str,
        default="./kanban.json",
        help="File path to the Kanban board.",
    )

    # Parse the command line arguments
    args = parser.parse_args()

    # Resolve args
    if args.create:
        from kanban_create_new import main as create_new

        create_new(args.file)
    elif args.verify:
        from kanban_verify import main as verify

        verify(args.file)
    elif args.list:
        from kanban_list import main as list_kanban

        list_kanban(args.file)
    else:
        print("Error: No command provided. Use --help for more information.")


if __name__ == "__main__":
    main()
