
import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # 1. Railway asigna un puerto dinámico, debemos leerlo
    port = int(os.environ.get("PORT", 5000))
    
    # 2. '0.0.0.0' permite que la app sea visible fuera del contenedor
    # 3. debug debe estar en False para producción
    app.run(host='0.0.0.0', port=port, debug=False)