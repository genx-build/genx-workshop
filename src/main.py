from dotenv import find_dotenv, load_dotenv

from src.engine import llm_engine

load_dotenv(find_dotenv())


from fastapi import FastAPI
from pydantic import BaseModel, StrictStr

app = FastAPI()


class ProfileQuery(BaseModel):
    query: StrictStr


@app.post("/info")
def get_info(body: ProfileQuery):
    return llm_engine(body.query)
