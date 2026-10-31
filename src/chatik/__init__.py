import os
import httpx

def main() -> None:
    api_key = os.getenv("API_KEY")

    print("Чат запущен. Для выхода введи /exit")

    while True:
        message = input("Ты: ").strip()

        if message == "/exit":
            break
        if not message:
            continue

        try:
            answer = ask_model(api_key, message)
        except httpx.HTTPStatusError as exc:
            print(f"Ошибка API: HTTP {exc.response.status_code}")
            continue
        except httpx.RequestError:
            print("Не удалось получить ответ: проверь соединение или повтори позже.")
            continue

        print(f"Ассистент: {answer}")


def ask_model(api_key: str, message: str) -> str:
    response = httpx.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "model": "openrouter/free",
            "messages": [
                {"role": "user", "content": message},
            ],
        },
        timeout=60.0,
    )
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]
    