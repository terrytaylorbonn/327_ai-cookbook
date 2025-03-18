from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4",
    # messages=[{"role": "user", "content": "Say this is a test"}],
    messages=[{"role": "user", "content": "is it safe to fly in nepal?"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
