from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import news, videos, search

app = FastAPI(title="AI News Hub API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(news.router, prefix="/news", tags=["news"])
app.include_router(videos.router, prefix="/videos", tags=["videos"])
app.include_router(search.router, prefix="/search", tags=["search"])

@app.get("/")
async def root():
    return {"message": "AI News Hub API", "version": "1.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
