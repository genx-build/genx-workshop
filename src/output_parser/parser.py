from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, StrictStr


class UserInfo(BaseModel):
    summery: StrictStr
    facts: list[StrictStr]
    connection_count: int


user_info_parser = PydanticOutputParser(pydantic_object=UserInfo)
