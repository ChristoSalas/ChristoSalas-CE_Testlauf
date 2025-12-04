def mini_rewrite(input_text):
    # Verbessert Text: einfache Großschreibung und Satzzeichenkorrektur
    import re
    text = input_text.strip()
    if not text:
        return ""
    text = text[0].upper() + text[1:]
    if not re.search(r'[.!?]$', text):
        text += '.'
    text = re.sub(r'\s+', ' ', text)
    return text

print (mini_rewrite("das ist ein richtiger text"))