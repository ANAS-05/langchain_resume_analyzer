import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()


class Config:
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
    LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.0"))


def get_llm():
    if not (os.getenv("OPENAI_API_KEY") or os.getenv("GEMINI_API_KEY")):
        raise ValueError(
            "No API key found. Set OPENAI_API_KEY or GEMINI_API_KEY in your .env file."
        )

    return init_chat_model(
        model=Config.LLM_MODEL,
        model_provider="google_genai",
        temperature=Config.LLM_TEMPERATURE,
    )
