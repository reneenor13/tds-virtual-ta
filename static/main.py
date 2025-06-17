from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Optional: redirect root to index.html
@app.get("/")
def read_index():
    return RedirectResponse(url="/index.html")
