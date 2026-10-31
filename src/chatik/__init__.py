def main() -> None:
    print("Чат запущен. Для выхода введи /exit")

    while True:
        message = input("Ты: ").strip()

        if message == "/exit":
            break
        if not message:
            continue

        print(f"Получено: {message}")