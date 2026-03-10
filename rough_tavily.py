from tavily import TavilyClient
from dotenv import load_dotenv
import os
load_dotenv()
# 👉 Paste your API key here
api_key = os.getenv("TAVILY_API_KEY")

# Initialize client
client = TavilyClient(api_key=api_key)

try:
    # Run a simple search
    response = client.search(
        query="What is melanoma?",
        max_results=3
    )

    print("✅ Tavily API is working!\n")

    # Print results nicely
    for i, result in enumerate(response["results"], 1):
        print(f"Result {i}:")
        print("Title  :", result["title"])
        print("URL    :", result["url"])
        print("Content:", result["content"][:150], "...")
        print("Score  :", result["score"])
        print("-" * 50)

except Exception as e:
    print("❌ Error:", e)
