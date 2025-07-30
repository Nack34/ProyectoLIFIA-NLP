from fastapi import FastAPI
app = FastAPI()

@app.get("/invertir_texto/")
def invertir_texto(texto: str):
    texto_invertido = texto[::-1]
    return {"respuesta": texto_invertido}