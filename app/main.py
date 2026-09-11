from fastapi import FastAPI

import subprocess
import json

app = FastAPI()


@app.get("/")
def root():
    return {"message": "AI Security Service is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/scan")
def scan():
    result = subprocess.run(
        ["semgrep", "scan", "--config=auto", "--json", "--exclude", "semgrep-results.json", "."],
        capture_output=True,
        text=True
    )

    return {
        "status": "success",
        "semgrep_output": json.loads(result.stdout)
    }