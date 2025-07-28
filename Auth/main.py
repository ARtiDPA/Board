"""Enter point."""

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def root():
    """_summary_
    Endpoint main page
    Returns:
        json: message about done
    """    
    return {'message':'Done', 'status':'running'}

if __name__=='__main__':
    uvicorn.run('main:app', host='0.0.0.0')