from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Application
    app_name: str = "Enterprise Knowledge Chat API"
    environment: str = "development"
    log_level: str = "INFO"

    # AWS
    aws_region: str = "eu-west-1"

    # Bedrock Converse API
    bedrock_model_id: str = "eu.amazon.nova-lite-v1:0"

    # Bedrock Knowledge Base
    bedrock_knowledge_base_id: str = ""

    # Retrieval
    bedrock_retrieval_results: int = 5
    max_retrieved_context_chars: int = 24000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
