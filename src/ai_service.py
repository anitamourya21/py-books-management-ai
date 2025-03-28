import httpx

OLLAMA_API_URL = "http://ollama:11434/v1/chat/completions"
MODEL_NAME = "tinyllama"

class AIService:
    @staticmethod
    async def generate_summary(book_title: str, book_content: str) -> str:
        """
        Generates a book summary using TinyLlama asynchronously.
        """
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": "Summarize books in a concise way."},
                {"role": "user", "content": f"Summarize the book '{book_title}': {book_content}"}
            ]
        }

        headers = {"Content-Type": "application/json"}

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(OLLAMA_API_URL, headers=headers, json=payload, timeout=30)
                response.raise_for_status()  # Raise exception for HTTP errors

                data = response.json()
                return data.get("choices", [{}])[0].get("message", {}).get("content", "No summary available.")

            except httpx.HTTPStatusError as e:
                return f"HTTP Error: {e.response.status_code} - {e.response.text}"
            except httpx.RequestError as e:
                return f"Request Error: {str(e)}"

