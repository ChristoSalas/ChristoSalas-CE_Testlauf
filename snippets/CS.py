def mini_text_improver(input_text):
    """Verbessert den gegebenen Text durch einfache Formatierungen."""
    # Split the text into sentences and capitalize the first letter of each sentence
    sentences = input_text.split('. ')
    improved_sentences = [s.capitalize() for s in sentences]
   
    # Join the sentences back together with proper punctuation
    improved_text = '. '.join(improved_sentences).strip()
    if not improved_text.endswith('.'):
        improved_text += '.'
   
    return improved_text
 
print (mini_text_improver("das ist ein richtiger text"))