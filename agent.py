import os

MODEL = "gemini-2.0-flash-exp"

PERSONA = """
You are a farm management assistant for a 40-acre farm in Yucca, Arizona.
Focus on livestock (cattle) and irrigation in a desert climate.
When discussing water, always convert 'inches' to total gallons required for the full 40 acres.
"""

def get_api_key() -> str:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is required. Set it in your shell or local .env loader before running the agent.")
    return api_key


def create_chat(api_key: str | None = None):
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key or get_api_key())
    return client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=PERSONA
        )
    )


def main() -> None:
    chat = create_chat()
    print("--- AZ Farm Agent Online (Type 'quit' to exit) ---")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit"]:
            print("Agent: Shutting down. Goodbye!")
            break

        response = chat.send_message(user_input)
        print(f"Agent: {response.text}\n")


if __name__ == "__main__":
    main()
