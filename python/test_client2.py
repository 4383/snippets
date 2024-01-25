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

# python python/test_client1.py  4,94s user 0,83s system 80% cpu 7,178 total

