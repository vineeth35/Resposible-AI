# Basic frequency analysis to distinguish AI vs Human text
def detect_ai_text(text):
    # AI often uses highly structured and predictable patterns
    repetitive_words = ["moreover", "furthermore", "in conclusion", "it is important to note"]
    score = sum(1 for word in repetitive_words if word in text.lower())
    
    if score >= 2:
        return "Likely AI-Generated"
    return "Likely Human-Written"

sample_text = "Moreover, it is important to note that the data reflects a trend. In conclusion, we must act."
print(f"Result: {detect_ai_text(sample_text)}")
