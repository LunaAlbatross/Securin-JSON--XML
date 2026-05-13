import json
import os
import html

def escape_xml(s):
    """
    Escapes special characters for XML.
    """
    if not isinstance(s, str):
        return s
    return html.escape(s)

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
        return f'<string{name_attr}>{escape_xml(data)}</string>'

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
    import sys
    
    # Check for correct number of arguments (script_name, input_file, output_file)
    if len(sys.argv) != 3:
        print("Usage: python3 json_to_xml.py <input.json> <output.xml>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Read the JSON input
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' was not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: The file '{input_file}' contains invalid JSON. {e}")
        sys.exit(1)
        
    # Convert to XML
    xml_output = json_to_xml(json_data)
    
    # Write the XML output
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml_output)
        print(f"Successfully converted '{input_file}' to '{output_file}'.")
    except Exception as e:
        print(f"Error: Failed to write to output file '{output_file}'. {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
