import requests
import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG)
logging.debug("this is debug")
logging.info("program started")
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')


def fetch_api(url):
    try:
        response = requests.get(url, timeout=3)

        # Raise error for 4xx or 5xx
        response.raise_for_status()

        try:
            data = response.json()
        except ValueError:
            print("❌ Invalid / Non-JSON response")
            return None

        print("✅ Success:", data)
        return data

    except requests.exceptions.Timeout:
        print("⏳ Request Timeout")
    except requests.exceptions.ConnectionError:
        print("❌ Host Unreachable")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
    except Exception as e:
        print(f"⚠ Unknown Error: {e}")


# -------------------------
# Testing
# -------------------------

good_url = "https://jsonplaceholder.typicode.com/todos/1"
bad_url = "http://unknown12345678.com"
non_json_url = "https://google.com"

print("\n--- GOOD URL TEST ---")
fetch_api(good_url)

print("\n--- BAD URL TEST ---")
fetch_api(bad_url)

print("\n--- NON-JSON URL TEST ---")
fetch_api(non_json_url)
