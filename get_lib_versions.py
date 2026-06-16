import importlib.metadata
packages = [
    "langgraph",
    "langchain_community",
    "langchain_core",
    "tavily-python",
    "wikipedia",
    "langchain_openai",
    "langchain-google-genai",
    "langchain-groq"
]
for package in packages:
    try:
        version = importlib.metadata.version(package)
        print(f"{package}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{package} not found")

