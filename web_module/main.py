from fastapi import FastAPI
app = FastAPI()

@app.get("/invertir_texto/")
def invertir_texto(texto: str):
    texto_invertido = texto[::-1]
    return {"original": texto, "respuesta": texto_invertido}


@app.get("/")
def default():
    return invertir_texto("Hello World")