# JSON to XML Project

This project is a Python tool that takes a JSON file and converts it into a specific XML format. It can be used as a **Command Line Interface (CLI)** tool or as a **Web API**.

## Features
- **CLI Mode**: Convert files directly from your terminal using standard Python libraries.
- **Web API Mode**: A modern FastAPI-based service with automatic Swagger documentation.
- **Recursive Conversion**: Handles deeply nested JSON objects and arrays.
- **XML Standards**: Correctly handles null values (using `<null/>`) and escapes special characters.

---

## 1. Command Line Interface (CLI)

The CLI version uses only standard Python libraries, so no extra installation is required.

### How to Run:
The script requires two arguments: the input JSON file and the desired output XML file.

```bash
python3 json_to_xml.py <input.json> <output.xml>
```

**Example:**
```bash
python3 json_to_xml.py examples/test1.json output.xml
```

---

## 2. Web API (FastAPI)

The Web API allows you to perform conversions through HTTP requests and provides an interactive interface.

### Prerequisites:
To run the Web API, you need to install the following dependencies:
```bash
pip install fastapi uvicorn
```

### How to Start the Server:
Run the `app.py` file:
```bash
python3 app.py
```
The server will start at `http://127.0.0.1:5000`.

### Interactive Documentation (Swagger UI):
Once the server is running, you can test the API directly from your browser:
- **Swagger UI**: [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)
- **ReDoc**: [http://127.0.0.1:5000/redoc](http://127.0.0.1:5000/redoc)

You can use the `/convert` endpoint to paste JSON data and receive raw XML in response.

---

## Project Structure
- `json_to_xml.py`: Core logic and CLI entry point.
- `app.py`: FastAPI server implementation.
- `examples/`: Sample JSON files for testing.
- `build.sh`: Simple script to prepare the environment.

## Design and Approach
I used a recursive function for the conversion. JSON is a tree-like structure, so recursion is the most efficient way to process nested objects and arrays. The code identifies data types (strings, numbers, booleans, nulls) and wraps them in their corresponding XML tags as per the requirements.
