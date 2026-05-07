# from dotenv import load_dotenv
# load_dotenv()

# import os

# class Config:

#     SECRET_KEY = os.getenv(
#         "SECRET_KEY",
#         "restaurant_secret_key"
#     )

#     SQLALCHEMY_DATABASE_URI = os.getenv(
#         "DATABASE_URL"
#     )

#     SQLALCHEMY_TRACK_MODIFICATIONS = False

#     SQLALCHEMY_ENGINE_OPTIONS = {
#         "pool_pre_ping": True,
#         "pool_recycle": 300,
#     }



import os
from dotenv import load_dotenv

# Carga las variables del archivo .env si existe (solo para local)
load_dotenv()

class Config:
    # 1. Clave secreta con valor por defecto
    SECRET_KEY = os.getenv("SECRET_KEY", "restaurant_secret_key")

    # 2. Obtener la URL de la base de datos
    # En Railway, asegúrate de que la variable se llame DATABASE_URL
    uri = os.getenv("DATABASE_URL")

    # FIX CRÍTICO: SQLAlchemy 1.4+ requiere 'postgresql://' 
    # pero algunas plataformas/configuraciones devuelven 'postgres://'
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    
    # Si 'uri' sigue siendo None (no hay variable), fallará con un mensaje claro
    SQLALCHEMY_DATABASE_URI = uri

    # 3. Configuraciones adicionales
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Recomendado para conexiones a bases de datos en la nube como Neon
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
        "connect_args": {"sslmode": "require"} # Requerido para Neon en la mayoría de los casos
    }



   