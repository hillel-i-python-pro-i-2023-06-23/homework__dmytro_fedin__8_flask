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


def delete_item(arg: int)->None:
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "DELETE FROM phone_book WHERE (pk=:arg);",
                {
                    "arg": arg,
                }
            )
