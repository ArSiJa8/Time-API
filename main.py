from fastapi import FastAPI, HTTPException
from datetime import datetime
from zoneinfo import ZoneInfo
import uvicorn

app = FastAPI(title="Time-API")

@app.get("/time/{area}/{city}")
async def get_time(area: str, city: str):
    timezone_str = f"{area}/{city}"
    try:
        # Zeit in der angegebenen Zeitzone abrufen
        now = datetime.now(ZoneInfo(timezone_str))
        return {
            "timezone": timezone_str,
            "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
            "iso": now.isoformat()
        }
    except Exception:
        raise HTTPException(status_code=404, detail="Zeitzone nicht gefunden. Format: Europe/Berlin")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
