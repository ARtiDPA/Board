"""Enter point."""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    """_summary_
    Endpoint main page
    Returns:
        json: message about done
    """
    return {'message': 'Done', 'status': 'running'}
