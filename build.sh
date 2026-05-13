#!/bin/bash
# Build script for JSON to XML Converter
# Since Python does not need compilation, we just make the script executable.

chmod +x json_to_xml.py

echo "Build complete! The script is now executable."
echo "You can run it using: python3 json_to_xml.py <input.json> <output.xml>"
