from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Static Folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve Homepage at "/"
@app.get("/", response_class=HTMLResponse)
async def serve_home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

# Reverse Text API
@app.post("/reverse")
async def reverse_text(request: Request):
    data = await request.json()
    text = data.get("text", "")
    reversed_text = text[::-1]
    styled_text = f"<b style='color:gold;'>{reversed_text}</b>"
    return JSONResponse({"status": "success", "reversed": styled_text})
