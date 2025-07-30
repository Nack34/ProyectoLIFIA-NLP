# ProyectoLIFIA-NLP

Este proyecto utiliza un entorno virtual gestionado con Conda y un servidor web basado en FastAPI.

## ⚙️ Configuración del entorno

1. Crear el entorno Conda desde el archivo `environment.yml`:
   ```bash
   conda env create -f environment.yml
   ```

2. Activar el entorno:
   ```bash
   conda activate LIFIA_NLP_env
   ```

3. (Opcional) Exportar el entorno actualizado si se agregaron dependencias:
   ```bash
   conda env export > environment.yml
   ```

---

## 🚀 Ejecución del servidor

Una vez activado el entorno, ubicarse dentro de la carpeta `web_module` y ejecutar:

```bash
uvicorn main:app --reload
```

Esto iniciará el servidor en modo desarrollo con recarga automática.
