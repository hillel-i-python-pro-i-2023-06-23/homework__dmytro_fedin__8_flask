from app.services.user_generator import generate_users


def generate_user_csv(amount: int = 100) -> None:
    for user in generate_users(amount=amount):
        print(f"{user.name}, {user.email}")
