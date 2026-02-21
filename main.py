from fastapi import FastAPI, HTTPException
from datetime import datetime
from zoneinfo import ZoneInfo
import uvicorn

app = FastAPI(
    title="World Time API",
    description="A lightweight microservice to retrieve current time across different timezones.",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
async def root():
    """Returns a simple welcome message and API status."""
    return {
        "status": "online",
        "message": "Welcome to the World Time API. Use /docs for full documentation.",
        "endpoints": ["/time/{area}/{city}"]
    }

@app.get("/time/{area}/{city}", tags=["Time Management"])
async def get_time(area: str, city: str):
    """
    Fetch current time for a specific geographic area and city.
    Example: /time/Europe/Berlin
    """
    timezone_str = f"{area}/{city}"
    try:
        now = datetime.now(ZoneInfo(timezone_str))
        return {
            "timezone": timezone_str,
            "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
            "timestamp": now.timestamp(),
            "iso": now.isoformat()
        }
    except Exception:
        raise HTTPException(
            status_code=404, 
            detail=f"Timezone '{timezone_str}' not found. Please use IANA format (e.g., Europe/London)."
        )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
