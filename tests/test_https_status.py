import requests
def test_status_code():
    url = "https://github.com/COMMANDO2406/CSVtoMySQL"
    try:
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        print("HTTP request successful with status code 200")
    except requests.RequestException as e:
        print(f"Request failed with exception: {e}")
        assert False, f"Request failed with exception: {e}"

if __name__ == "__main__":
    test_status_code()
