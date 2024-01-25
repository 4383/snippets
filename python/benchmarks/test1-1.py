import requests

headers = {
    'User-Agent': 'simple_requests_client_without_session',
}

def main():
    for i in range(5000):
        response = requests.get('http://localhost:8088', headers=headers)
        print(response.text)

if __name__ == "__main__":
    main()

# 5,53s user 0,96s system 62% cpu 10,441 total
