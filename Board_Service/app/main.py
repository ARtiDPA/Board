"""Enter point."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """_summary_
    Board main page
    Returns:
        json: message
    """
    return {"service": "Board", "status": "running"}
