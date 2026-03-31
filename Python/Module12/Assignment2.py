import requests


def main():
    api_key = "979bcef54ed21ca9eea49b5399e4a575"

    municipality = input("Enter municipality name: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            description = data['weather'][0]['description']
            temperature = data['main']['temp']

            print(f"Weather: {description}")
            print(f"Temperature: {temperature} Celsius")

        elif response.status_code == 401:
            print("Error: Invalid API key. Please check your key.")
        elif response.status_code == 404:
            print("Error: Municipality not found.")
        else:
            print(f"Error: HTTP {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")


main()