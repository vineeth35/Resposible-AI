# Checking if LLM output matches a database of copyrighted snippets
def check_copyright_overlap(llm_output, reference_texts):
    for ref in reference_texts:
        if ref in llm_output:
            return True, ref
    return False, None

copyrighted_works = ["The quick brown fox jumps over the lazy dog.", "To be or not to be."]
generated_output = "The model said: To be or not to be."

violation, source = check_copyright_overlap(generated_output, copyrighted_works)
if violation:
    print(f"Potential Copyright Issue: Matches source '{source}'")
