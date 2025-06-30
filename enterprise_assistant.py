"""
enterprise_assistant.py

A formal enterprise-grade chatbot using OpenAI GPT models.
Intended for integration with corporate systems to provide technical
assistance and knowledge retrieval.

Requirements:
    - Python 3.9+
    - openai>=1.0

Environment:
    - OPENAI_API_KEY must be set

Usage:
    python enterprise_assistant.py
"""

from openai import OpenAI
import os

def initialize_client():
    """
    Initialize the OpenAI client with environment-based credentials.
    """
    return OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def enterprise_chat():
    """
    Main loop for the enterprise assistant.
    """
    client = initialize_client()

    messages = [
        {
            "role": "system",
            "content": (
                "You are a technical enterprise assistant. "
                "Respond in a professional, formal tone. "
                "Provide strictly technical and factual information. "
                "Avoid personal opinions."
            )
        }
    ]

    print("Enterprise Assistant ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ("exit", "quit"):
            print("Session terminated.")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        answer = response.choices[0].message.content
        print(f"Assistant: {answer}\n")
        messages.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    enterprise_chat()
