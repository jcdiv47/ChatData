from pathlib import Path

persist_path = Path(__file__).parent.parent / "db"
persist_path.mkdir(parents=True, exist_ok=True)
PERSIST_DIRECTORY = str(persist_path)

OPENAI_MODEL = 'gpt-3.5-turbo'
EMBEDDING_MODEL = "text-embedding-ada-002"
EMBEDDING_MODEL_MAX_TOKEN = 8191  # for "text-embedding-ada-002"
