def hello_world(name: str) -> None:
    """Print a personalized greeting message.

    Args:
        name (str): The name of the person to greet.

    Returns:
        None
    """
    print(f"Hello, {name}!")

if __name__ == "__main__":
    hello_world("Alice")