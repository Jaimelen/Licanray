from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root (req: Request):
    return templates.TemplateResponse("index.html", {
        "request": req,
    })

@app.get("/inicio", response_class=HTMLResponse)
def root (req: Request):
    return templates.TemplateResponse("index.html", {
        "request": req,
    })

@app.get("/comprar", response_class=HTMLResponse)
def root (req: Request):
    return templates.TemplateResponse("comprar.html", {
        "request": req,
    })    

@app.get("/arrendar", response_class=HTMLResponse)
def root (req: Request):
    return templates.TemplateResponse("arriendo.html", {
        "request": req,
    })

@app.get("/login", response_class=HTMLResponse)
def root (req: Request):
    return templates.TemplateResponse("login.html", {
        "request": req,
    })

@app.get("/registro", response_class=HTMLResponse)
def root (req: Request):
    return templates.TemplateResponse("registro.html", {
        "request": req,
    })

@app.get("/recuperar", response_class=HTMLResponse)
def root (req: Request):
    return templates.TemplateResponse("recuperar.html", {
        "request": req,
    })

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80)
