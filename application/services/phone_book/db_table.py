from application.services.phone_book import DBConnection


def create_table() -> None:
    with DBConnection() as connection:
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS phone_book (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    number TEXT NOT NULL
                )
                """
            )


def add_user(args: dict)->str:
    with DBConnection() as connection:
        with connection:
            connection.execute(
                'INSERT INTO phone_book (id, name, number) VALUES (:id, :name, :number);',
                {
                    "id": args["id"],
                    "name": args["name"],
                    "number": args["number"]
                }
            )

    return "Item added"
