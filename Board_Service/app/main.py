"""Enter point."""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def read_root():
    """_summary_
    Board main page
    Returns:
        json: status
    """
    return {'service': 'Board', 'status': 'running'}
