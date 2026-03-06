# Program to flag potential ethical risks in LLM outputs
def assess_llm_risks(output_text):
    # List of high-risk keywords that might indicate harmful or biased content
    risk_keywords = ["danger", "unethical", "biased", "confidential", "illegal"]
    detected_risks = [word for word in risk_keywords if word in output_text.lower()]
    
    risk_level = "Low"
    if len(detected_risks) > 2:
        risk_level = "High"
    elif len(detected_risks) > 0:
        risk_level = "Medium"
        
    return {
        "risk_level": risk_level,
        "flagged_terms": detected_risks,
        "requires_human_review": risk_level != "Low"
    }

# Example Assessment
model_output = "This system uses confidential data which might lead to biased results."
audit_results = assess_llm_risks(model_output)

print(f"Risk Assessment Report:")
print(f"- Overall Risk: {audit_results['risk_level']}")
print(f"- Flagged Terms: {', '.join(audit_results['flagged_terms'])}")
print(f"- Action Required: {'Yes' if audit_results['requires_human_review'] else 'No'}")
