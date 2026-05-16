from fastapi import FastAPI, HTTPException, Response
from typing import Any, Dict
from json_to_xml import json_to_xml
import uvicorn

app = FastAPI(
    title="JSON to XML Converter API",
    description="A simple API to convert JSON data to a specific XML format.",
    version="1.0.0"
)

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Welcome to the JSON to XML Converter API. Go to /docs for the Swagger UI."}

@app.post("/convert")
async def convert_json(data: Dict[str, Any]):
    try:
        if not data:
            raise HTTPException(status_code=400, detail="No JSON data provided")
            
        xml_output = json_to_xml(data)
        
        return Response(content=xml_output, media_type="application/xml")
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Conversion error: {str(e)}")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
