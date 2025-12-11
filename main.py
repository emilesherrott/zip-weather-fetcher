from services.fetch_service import FetchService
from services.data_store import JSONDataStore
from typing import Dict, Any

JSON_PATH: str = "data/location_weather.json"

if __name__ == "__main__":
    # Fetch ZIP and current weather, save to JSON
    combined_data: Dict[str, Any] = FetchService.run(JSON_PATH)
    print("ZIP and Current Weather:")
    print(combined_data)

    # Read back from JSON
    store: JSONDataStore = JSONDataStore(JSON_PATH)
    print("\nReading back from JSON:")
    print(store.read())
