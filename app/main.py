from fastapi import FastAPI

app = FastAPI(title="WW Exchange")


@app.get("/")
def read_root():
    return {"message": "Welcome to WW Exchange API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
