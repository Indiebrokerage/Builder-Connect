from pydantic import BaseSettings
class Settings(BaseSettings):
    api_base: str = "http://localhost:8000"
    figma_token: str = ""
    figma_file_id: str = ""
    brand_list: str = "default,acme,greenfield"
    factory_api: str = ""
    factory_token: str = ""
    mls_corelogic_key: str = ""
    reso_web_api_key: str = ""
    menards_api_key: str = ""
    lowes_api_key: str = ""
    homedepot_api_key: str = ""
    stripe_secret: str = ""
    class Config: env_file = ".env"; env_file_encoding = "utf-8"
settings = Settings()
