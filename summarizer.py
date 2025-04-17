from transformers import pipeline

# Load the model once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    if len(text.strip()) == 0:
        return "No content to summarize."
    # Limit input to 1024 tokens (model limit)
    if len(text) > 3000:
        text = text[:3000]
    result = summarizer(text, max_length=30, min_length=10, do_sample=False)
    return result[0]['summary_text']
