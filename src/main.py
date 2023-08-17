from dotenv import find_dotenv, load_dotenv

from src.engine import llm_engine

load_dotenv(find_dotenv())


from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, StrictStr

app = FastAPI()


class ProfileQuery(BaseModel):
    query: StrictStr


@app.post("/info")
def get_info(body: ProfileQuery):
    response = llm_engine(body.query)
    if response is None:
        raise HTTPException(
            status_code=404,
            detail="can not find proper user profile( write better query)",
        )
    print(128 * "#")
    return response
