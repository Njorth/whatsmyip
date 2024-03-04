import requests
from pprint import pprint


if __name__ == "__main__":
    r = requests.get("http://ipinfo.io/")
    data = r.json()
    print(f"{ data['ip'] } ({data['country'] })")

