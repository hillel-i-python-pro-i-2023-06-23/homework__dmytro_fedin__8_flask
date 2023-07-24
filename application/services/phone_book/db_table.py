import sqlite3

from flask import Response

from application.services.phone_book import DBConnection


def create_table() -> None:
    with DBConnection() as connection:
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS phone_book (
                    pk INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    number TEXT NOT NULL
                )
                """
            )


def add_item(args: dict)->None:
    with DBConnection() as connection:
        with connection:
            connection.execute(
                'INSERT INTO phone_book (name, number) VALUES (:name, :number);',
                {
                    "name": args["name"],
                    "number": args["number"]
                }
            )


def read_all()->str:
    with DBConnection() as connection:
        items = connection.execute(
            "SELECT * FROM phone_book;"
        ).fetchall()

    return "<br>".join(
        [
            f'{item["pk"]}: {item["name"]} - {item["number"]}' for item in items
        ]
    )


def read_item(arg: int)->sqlite3.Row | None:
    with DBConnection() as connection:
        item = connection.execute(
            "SELECT * FROM phone_book WHERE (pk=:arg);",
            {
                "arg": arg,
            }
        ).fetchone()

        return item


def delete_item(arg: int)->None:
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "DELETE FROM phone_book WHERE (pk=:arg);",
                {
                    "arg": arg,
                }
            )


def update_item(args: dict[str], pk: int)->None:
    with DBConnection() as connection:
        with connection:
            name = args.get("name")
            number = args.get("number")
            if name is None and number is None:
                return Response(
                    "At least one arg needed",
                    status=400,
                )

            args_for_request = []

            if name is not None:
                args_for_request.append("name=:name")
            if number is not None:
                args_for_request.append("number=:number")

            args_2 = ", ".join(args_for_request)

            connection.execute(
                f"UPDATE phone_book SET {args_2} WHERE pk=:pk;",
                {
                    "pk": pk,
                    "name": name,
                    "number": number,
                }
            )