# Simple simulation of LLM capabilities like text generation and summarization
def summarize_text(text):
    # Simulating a summarization logic (taking the first sentence as a summary)
    summary = text.split('.')[0] + "."
    return f"Summary: {summary}"

def generate_response(prompt):
    # Simulating context-aware response generation
    responses = {
        "hello": "Greetings! How can I assist you with Responsible AI today?",
        "explain rai": "Responsible AI (RAI) is the practice of designing and deploying AI that is ethical and transparent."
    }
    return responses.get(prompt.lower(), "I am an AI trained to discuss ethical system design.")

# Usage
long_text = "Generative AI can create new content. It is powered by Large Language Models."
print(summarize_text(long_text))
print(generate_response("explain rai"))
