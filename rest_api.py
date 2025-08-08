import requests
import json

BASE_URL = "http://localhost:5000"

def test_api():
    """Test the Flask REST API endpoints"""

   
    get_user_id = 1
    update_user_id = 2
    delete_user_id = 3

    print("Testing Flask REST API")
    print("=" * 50)

    
    print("\n1. Getting all users:")
    response = requests.get(f"{BASE_URL}/api/users")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

   
    print("\n2. Creating a new user:")
    new_user = {
        "name": "Alice Johnson",
        "email": "alice@example.com"
    }
    response = requests.post(f"{BASE_URL}/api/users", json=new_user)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    
    print(f"\n3. Getting user with ID {get_user_id}:")
    response = requests.get(f"{BASE_URL}/api/users/{get_user_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


    print(f"\n4. Updating user with ID {update_user_id}:")
    update_data = {"name": "Jane Doe Updated"}
    response = requests.put(f"{BASE_URL}/api/users/{update_user_id}", json=update_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    
    print(f"\n5. Deleting user with ID {delete_user_id}:")
    response = requests.delete(f"{BASE_URL}/api/users/{delete_user_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

  
    print("\n6. Getting all users after changes:")
    response = requests.get(f"{BASE_URL}/api/users")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:

        print("Error: Could not connect to the API. Make sure the Flask app is running on http://localhost:5000")
