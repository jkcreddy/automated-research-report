from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os
from research_and_analysts.api.routes import report_routes
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(BASE_DIR))

app = FastAPI(title="Autonomous Report Generator UI")

app.mount("/static", StaticFiles(directory=os.path.join(ROOT_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.templates = templates

# 🔹 ADD THIS FUNCTION
def basename_filter(path: str):
    return os.path.basename(path)

# 🔹 REGISTER FILTER
templates.env.filters["basename"] = basename_filter

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#health check have been added
@app.get("/health")
async def health_check():
    """Health check endpoint for container orchestration"""
    return {
        "status": "healthy",
        "service": "autonomous-report-generator-ui",
        "timestamp": datetime.now().isoformat()
    }

# Register Routes
app.include_router(report_routes.router)
