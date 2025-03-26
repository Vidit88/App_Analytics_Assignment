import requests

def get_location_data():
    try:
        
        print("Fetching location data...")
        response = requests.get('https://ipapi.co/json/')
        response.raise_for_status()
        location_data = response.json()

        
        lat = location_data.get('latitude')
        lon = location_data.get('longitude')

        if lat is None or lon is None:
            raise ValueError("Latitude or Longitude not found in the API response.")

        print(f"Location fetched successfully - Latitude: {lat}, Longitude: {lon}")

        
        print("Sending data to the second API for further information...")
        post_data = {"lat": lat, "lon": lon}
        post_response = requests.post('http://3.255.195.197/api/q1', json=post_data)
        post_response.raise_for_status()
        result_data = post_response.json()

        
        display_name = result_data.get('display_name', 'N/A')
        city = result_data.get('city', 'N/A')

        print(f"Display Name: {display_name}")
        print(f"City: {city}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the API request: {e}")
    except ValueError as e:
        print(f"Data Error: {e}")

if __name__ == "__main__":
    get_location_data()
