import json
import os

def json_to_xml(data, name=None):
    """
    Recursively converts JSON data types to specific XML tags.
    """
    # Create the name attribute string if a name is provided
    name_attr = f' name="{name}"' if name is not None else ''

    if isinstance(data, dict):
        xml = f'<object{name_attr}>'
        for key, val in data.items():
            xml += json_to_xml(val, key)
        xml += '</object>'
        return xml

    elif isinstance(data, list):
        xml = f'<array{name_attr}>'
        for val in data:
            xml += json_to_xml(val)  # List items do not have names
        xml += '</array>'
        return xml

    elif isinstance(data, str):
        return f'<string{name_attr}>{data}</string>'

    elif isinstance(data, bool):
        # JSON booleans are true/false, Python's are True/False
        str_val = str(data).lower()
        return f'<boolean{name_attr}>{str_val}</boolean>'

    elif isinstance(data, (int, float)):
        return f'<number{name_attr}>{data}</number>'

    elif data is None:
        return f'<null{name_attr}/>'

    else:
        # Fallback for any unknown types
        return f'<unknown{name_attr}>{data}</unknown>'

def main():
    input_file = "example_input.json"
    output_file = "my_output.xml"
    
    print(f"Reading {input_file}...")
    try:
        with open(input_file, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Make sure the file exists in the JSON-XML directory.")
        return

    print("Converting JSON to XML...")
    # The root of the JSON file is typically an object (dict)
    xml_output = json_to_xml(json_data)

    print(f"Writing to {output_file}...")
    with open(output_file, 'w') as f:
        f.write(xml_output)
    
    print("Conversion complete!")
    
    # Read the expected output to compare
    try:
        with open('example_output.xml', 'r') as f:
            expected_output = f.read().strip()
            
        if xml_output == expected_output:
            print("\nSUCCESS: The generated XML matches exactly with example_output.xml!")
        else:
            print("\nWARNING: The generated XML differs from example_output.xml.")
            print("\nGenerated:")
            print(xml_output)
            print("\nExpected:")
            print(expected_output)
    except FileNotFoundError:
        print("\nCould not find example_output.xml to verify against.")

if __name__ == "__main__":
    main()
