from __future__ import annotations

from io import BytesIO
from typing import TYPE_CHECKING, Any

import streamlit as st

if TYPE_CHECKING:
    import httpx


def check_api_running(client: httpx.Client, /) -> None:
    """
    Check whether the API is running on the given `base_url`, if not stop the streamlit app.
    """
    res = client.get("/?checkFromStreamlitApp=true")
    if res.status_code == 200:
        return
    st.error("Check whether API is running or not...", icon="💥")
    st.stop()


def one_shot(client: httpx.Client, /, image_bytes: bytes) -> dict[str, Any]:
    check_api_running(client)
    res = client.post(
        "/one-shot",
        files={
            "image": BytesIO(image_bytes),
        },
        timeout=30,
    )
    if res.status_code == 200:
        return res.json()
    st.error("Bad response from API.", icon="💥")
    st.stop()
