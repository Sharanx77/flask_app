import requests
import json

BASE_URL = "http://localhost:5000"

def test_api():
    """Test the Flask REST API endpoints"""

    # User IDs to use in the tests
    get_user_id = 1
    update_user_id = 2
    delete_user_id = 3

    print("Testing Flask REST API")
    print("=" * 50)

    # Test GET all users
    print("\n1. Getting all users:")
    response = requests.get(f"{BASE_URL}/api/users")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Test POST - Create new user
    print("\n2. Creating a new user:")
    new_user = {
        "name": "Alice Johnson",
        "email": "alice@example.com"
    }
    response = requests.post(f"{BASE_URL}/api/users", json=new_user)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Test GET specific user
    print(f"\n3. Getting user with ID {get_user_id}:")
    response = requests.get(f"{BASE_URL}/api/users/{get_user_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Test PUT - Update user
    print(f"\n4. Updating user with ID {update_user_id}:")
    update_data = {"name": "Jane Doe Updated"}
    response = requests.put(f"{BASE_URL}/api/users/{update_user_id}", json=update_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Test DELETE user
    print(f"\n5. Deleting user with ID {delete_user_id}:")
    response = requests.delete(f"{BASE_URL}/api/users/{delete_user_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Test GET all users again to see changes
    print("\n6. Getting all users after changes:")
    response = requests.get(f"{BASE_URL}/api/users")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the Flask app is running on http://localhost:5000")