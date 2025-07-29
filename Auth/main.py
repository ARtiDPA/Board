"""Enter point."""

from fastapi import FastAPI
import uvicorn
from tokens.tokens import create_access_token, create_refresh_token, verify_token

app = FastAPI()

@app.get('/')
async def root():
    """_summary_
    Endpoint main page
    Returns:
        json: message about done
    """    
    return {'message':'Done', 'status':'running'}

@app.post('/login')
async def login() -> dict:
    """_summary_
    Login and getting tokens endpoint test verion
    Returns:
        dict: message about done and tokens
    """    
    user_id = 123
    role = 'admin'

    access_token = create_access_token(user_id, role)
    refresh_token = create_refresh_token(user_id, role)

    return {
        'message': 'Login successful',
        'access_token': access_token,
        'refresh_token': refresh_token
    }

@app.post('/refresh')
async def refresh(refresh_token: str)->dict:
    """_summary_
    Refreshing access tokenn endpoint
    Args:
        refresh_token (str): refresh token

    Returns:
        dict: error message or new access token
    """    
    token_data  = verify_token(refresh_token)
    if not token_data:
        return {
                'message':'Invalid token',
            }

    if token_data['type'] != 'refresh':
        return{
            'message':'Invalid token',
        }
        
    new_access_token = create_access_token(token_data ['user_id'],token_data ['role'])
    return {
        'message':'Refresh successful',
        'access_token':new_access_token
    }

@app.get('/profile')
async def get_profile(access_token: str)->dict:
    """_summary_
    Getting user's information endpoint
    Args:
        access_token (str): access token

    Returns:
        dict: error message or user's information
    """    
    token_data  = verify_token(access_token)
    if not token_data:
        return {
                'message':'Invalid token',
            }

    if token_data['type'] != 'access':
        return{
            'message':'Invalid token',
        }
        
    return {
        'message':'Access allowed',
        'user_id':token_data['user_id'],
        'role':token_data['role']
    }

if __name__=='__main__':
    uvicorn.run('main:app', host='0.0.0.0')