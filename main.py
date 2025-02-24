from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/shorten")
def shorten_url(url: str = Query(..., title="URL to Shorten")):
    """Shortens a given URL using TinyURL API"""
    try:
        response = requests.get(f"https://tinyurl.com/api-create.php?url={url}")
        if response.status_code == 200:
            return {"short_url": response.text}
        else:
            return {"error": "Failed to shorten URL"}
    except Exception as e:
        return {"error": str(e)}
