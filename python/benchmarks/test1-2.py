import requests

headers = {
    'User-Agent': 'simple_requests_client_with_session',
}

s = requests.Session()

def main():
    for i in range(5000):
        response = s.get('http://localhost:8088', headers=headers)
        print(response.text)

if __name__ == "__main__":
    main()

# 4,24s user 0,28s system 74% cpu 6,071 total
