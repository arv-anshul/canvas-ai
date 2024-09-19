# Canvas Calculator AI

<p align=center>
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff" alt="Docker">
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=fff" alt="FastAPI">
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?logo=googlegemini&logoColor=fff" alt="Google Gemini">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=fff" alt="LangChain">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" alt="Python">
</p>

Parse and Analyse image containing mathematical expression or problem (it can be in a drawing format) using AI to give a
structured response by leveraging Langchain framework. Also created API out of it using FastAPI which has containerized
with Docker.

## Prompt Examples

### Example 1

![image](images/expr.png)

```json
{
  "expression": "x=3;y=4;x+y=?",
  "result": "7",
  "explanation": "The sum of x and y is 7"
}
```

### Example 2

![image](images/car-tree.png)

```json
{
  "expression": "10 km/hr * (50 meters / 1000 meters/km) * (3600 seconds / 1 hour)",
  "result": "18 seconds",
  "explanation": "The car is travelling at 10 km/hr and it has to cover 50 meters, so we can calculate the time it takes to cover the distance."
}
```

[**See more examples on my website!**](https://arv-anshul.github.io/project/canvas-ai)

### Features

- [x] :framed_picture: Analyse one image at a time and return a structured response.
- [x] :boom: Create API out of it using FastAPI.
- [x] :whale: Containerize FastAPI app using Docker.
- [ ] Create frontend using Streamlit or else.
- [ ] Add more prompts to process images in different endpoint.
