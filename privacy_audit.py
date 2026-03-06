# Simple data anonymization script
def anonymize_dataset(df, columns_to_mask):
    for col in columns_to_mask:
        df[col] = df[col].apply(lambda x: "CONFIDENTIAL")
    return df

raw_data = pd.DataFrame({
    'Name': ['John Doe', 'Jane Smith'],
    'Email': ['john@example.com', 'jane@example.com'],
    'Purchase': [100, 200]
})

anonymized = anonymize_dataset(raw_data, ['Name', 'Email'])
print(anonymized)
