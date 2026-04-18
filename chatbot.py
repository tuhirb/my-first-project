import anthropic

client = anthropic.Anthropic()

print("Claude Chatbot — type 'quit' to exit\n")

conversation_history = []

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == "quit":
        print("Bye!")
        break
    
    if not user_input:
        continue

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    print(conversation_history)

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system="You are a pirate. Always respond in pirate speak. Always question everything i tell you before believing it. But keep your response concise",
        messages=conversation_history
    )

    reply = response.content[0].text

    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    print(f"\nClaude: {reply}\n")