import requests


def get_status(url: str) -> int:
    response = requests.get(url)
    return response.status_code


def main() -> None:
    url = "https://httpbin.org/get"
    status = get_status(url)

    print(f"Статус сайту: {status}")


if __name__ == "__main__":
    main()