import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from the .env file at the project root
load_dotenv()

class Config:
    """Centralized configuration for the Candidate Match Analyzer."""
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # LLM Settings
    # We default to gpt-4o-mini as it offers an excellent balance of speed, cost, and reasoning.
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
    
    # Temperature 0 is crucial here. We want factual data extraction, not creative writing.
    LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.0"))

def get_llm() -> ChatOpenAI:
    """Instantiates and returns the configured LangChain Chat Model."""
    if not Config.OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY environment variable is missing. "
            "Please ensure your .env file is set up correctly."
        )
        
    return ChatOpenAI(
        model=Config.LLM_MODEL,
        temperature=Config.LLM_TEMPERATURE,
        api_key=Config.OPENAI_API_KEY
    )