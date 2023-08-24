from dotenv import find_dotenv, load_dotenv
from src.engine import llm_engine
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, StrictStr
from .logger import get_logger

load_dotenv(find_dotenv())
logger = get_logger(__file__)
app = FastAPI()


class ProfileQuery(BaseModel):
    query: StrictStr


@app.post("/info")
def get_info(body: ProfileQuery):
    logger.info(f"query: {body.query}")
    response = llm_engine(body.query)
    if response is None:
        raise HTTPException(status_code=404,
                            detail="can not find proper user profile( write better query)")
    logger.info(f"response: {response}")
    return response
