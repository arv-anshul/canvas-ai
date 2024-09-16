from __future__ import annotations

from typing import TYPE_CHECKING

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

from app.genai import gemini_llm

if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel


ONE_SHOT_ANALYSER_PROMPT = """
You are an excellent mathematician. I am going to provide you images where some mathematical expressions
are written or drawn related to mensuration, linear algebra, calculus or BODMAS. So you have solve
them and return the answer in required JSON format.

{
  "expression": "the parsed expresion from image",
  "result": "result of expression (include units if require)",
  "explanation": "explain the result in less than 50 words"
}

> DO NOT USE MARKDOWN FORMATTING OR QUOTING.
> JUST RETURN THE REQUIRED JSON RESPONSE.
"""


class OneShotResponse(BaseModel):
    expression: str = Field(
        description="the parsed expresion from image",
    )
    result: str = Field(
        description="result of expression (include units if require)",
    )
    explanation: str = Field(
        description="explain the result in less than 50 words",
    )


async def one_shot_image_analyser(
    llm: BaseChatModel,
    image_base64: bytes,
) -> OneShotResponse:
    prompt = HumanMessage(
        [
            {
                "type": "image_url",
                "image_url": f"data:image/jpeg;base64,{image_base64.decode()}",
            },
        ],
    )

    chain = llm | JsonOutputParser(pydantic_object=OneShotResponse)
    response = await chain.ainvoke([SystemMessage(ONE_SHOT_ANALYSER_PROMPT), prompt])
    return OneShotResponse(**response)


if __name__ == "__main__":
    import asyncio
    import base64
    from pathlib import Path

    image_path = Path("backend/images/car-tree.png")
    model = gemini_llm()

    response = asyncio.run(
        one_shot_image_analyser(
            model,
            base64.b64encode(image_path.read_bytes()),
        ),
    )
    print(type(response), " : ", response)
