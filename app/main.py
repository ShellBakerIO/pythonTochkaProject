from fastapi import FastAPI

app = FastAPI(title="WW Fond")


@app.get("/")
def read_root():
    return {"message": "Welcome to Toy Exchange API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
