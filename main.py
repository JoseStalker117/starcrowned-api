from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importamos los routers de cada modelo
from routers import admin, alumno, maestro, default

app = FastAPI(
    title="starcrowned-api",
    description="API REST de starcrowned-app por modelos",
    version="1.0.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluimos los routers
app.include_router(alumno.router)
app.include_router(maestro.router)
app.include_router(admin.router)
app.include_router(default.router)

# Ruta raíz
@app.get("/")
async def root():
    return {"message": "Servicio en linea correctamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=7777, reload=True)
    