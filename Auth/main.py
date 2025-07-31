"""Enter point."""

from fastapi import FastAPI
import uvicorn
from tokens.tokens import create_access_token, create_refresh_token, verify_token

app = FastAPI()
