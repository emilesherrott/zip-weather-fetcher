Fetching ZIP Code and Weather – How It Works

This project is designed to fetch your current ZIP/postal code and the current weather conditions using two free APIs, and save the results in a JSON file. It is modular, object-oriented, and easy to extend.

Key Components
1. APIClient

A generic class to make GET requests to any API.

Input: API URL (and optional endpoint)

Output: JSON response (or error information)

Used by FetchService to fetch location and weather data.

2. JSONDataStore

Handles reading and writing JSON files.

Input: File path, dictionary of data

Output: Reads dictionary from JSON, writes dictionary to JSON

Ensures directory exists before writing.

3. FetchService

Orchestrates the workflow.

Steps:

Use APIClient to fetch location (ZIP code) from ip-api.com.

Extract latitude and longitude.

Use APIClient to fetch current weather from wttr.in using latitude and longitude.

Collect ZIP code and current weather into a dictionary.

Save the dictionary to JSON using JSONDataStore.

Returns the combined dictionary of ZIP code and weather.

4. main.py

Calls FetchService.run() with the JSON file path.

Prints combined data to the console.

Reads back from the JSON file using JSONDataStore.



```
Data Flow – Step by Step
main.py
   │
   ▼
FetchService.run(json_path)
   │
   ├─► APIClient -> Fetch location from ip-api.com
   │         │
   │         ▼
   │    location dict (zip, lat, lon)
   │
   ├─► APIClient -> Fetch weather from wttr.in using lat/lon
   │         │
   │         ▼
   │    weather dict (current conditions)
   │
   ▼
Combine location + weather into dict
   │
   ▼
JSONDataStore.write() -> Saves dict to JSON file
   │
   ▼
JSONDataStore.read() -> Reads dict back (optional)
   │
   ▼
Output to console
```


Summary of Interactions
Component	Uses / Calls	Returns / Outputs
main.py	FetchService.run	Combined dict
FetchService	APIClient	JSON data from APIs
FetchService	JSONDataStore	Writes combined data to file
JSONDataStore	None	Reads/writes JSON
APIClient	None	Returns API response as dict
Key Points

Each class has a single responsibility.

APIs are decoupled from JSON handling.

Data is readable and persistent via JSON.

The workflow can be extended easily to include more APIs, e.g., news, air quality, etc.