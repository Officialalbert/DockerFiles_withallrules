import requests
import datetime

def main():

    response = requests.get('https://timeapi.io/api/Time/current/zone?timeZone=Europe/Moscow')
    if response.status_code == 200:
        print("Hello, Docker! 🐳")
        print(f"текущее время по Moscow: {response.json().get('dateTime')}")
    else:
        print("Не удалось получить время, но привет всё равно!")

if __name__ == "__main__":
    main()
