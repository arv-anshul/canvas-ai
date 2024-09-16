import base64
import time
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, File, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from langchain_core.globals import set_verbose
from langchain_core.language_models import BaseChatModel

from app.genai import gemini_llm
from app.one_shot import (
    OneShotResponse,
    one_shot_image_analyser,
)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    set_verbose(True)
    yield


app = FastAPI(
    title="Canvas Calculator AI",
    description="Calculate your canvas/drawing using AI.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(500)
async def handle_unexpected_errors(_request: Request, e: Exception):
    """Handle unexpected errors and format it to return as pretty response."""
    return JSONResponse(
        status_code=500,
        content={"errorType": type(e).__name__, "message": str(e)},
    )


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.3f} seconds"
    return response


@app.get("/")
async def root():
    return {
        "creator": {
            "name": "Anshul Raj Verma",
            "portfolio": "https://arv-anshul.github.io/about",
            "github": "https://github.com/arv-anshul",
            "linkedin": "https://linkedin.com/in/arv-anshul",
        },
        "message": "server is running...",
    }


@app.post("/one-shot", response_model=OneShotResponse)
async def one_shot_analyser_route(
    image: UploadFile = File(
        media_type="image/png;image/jpg;image/jpeg",
    ),
    model: BaseChatModel = Depends(gemini_llm),
) -> OneShotResponse:
    """Analyse the input image with one shot prompt."""
    image_base64 = base64.b64encode(await image.read())
    response = await one_shot_image_analyser(model, image_base64)
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",  # noqa: S104
        port=8080,
    )
