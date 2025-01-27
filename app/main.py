from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from demo_boilerplate import method_1
app = FastAPI(title="My FastAPI App")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modify this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def root(arg_1: str, arg_2: str, arg_3: str):
    variable = await method_1(arg_1, arg_2, arg_3)
    return variable



@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080) 