from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

# Mount the static folder
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def root():
    return RedirectResponse("/index.html")


