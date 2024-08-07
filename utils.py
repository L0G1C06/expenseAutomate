from paddleocr import PaddleOCR
from openai import OpenAI

# Inicialize o cliente OpenAI
client = OpenAI()

# Inicialize o OCR do PaddleOCR
ocr = PaddleOCR(lang='pt')

def print_all_words(result):
    words = []
    for sublist in result:
        if isinstance(sublist, list):
            words.extend(print_all_words(sublist))
        elif isinstance(sublist, tuple):
            word = sublist[0]
            words.append(word)
    return words

def makeOCR(image):
    result = ocr.ocr(image)
    words = print_all_words(result=result)
    text = ' '.join(words)  # Converte a lista de palavras em uma string
    return text

def classify(text):
    query = f"""
    baseado no seguinte texto
    {text}
    me classifique que tipo de gasto que eu tive baseado nas seguintes categorias

    Carro
    Supermercado
    Farmácia
    Educação
    Internet
    Energia
    Gás
    Condomínio
    Pet
    Lazer
    Vestimenta
    Saúde
    Voluntariado
    Diversos
    Apartamento
    Água

    e me retorne o valor total gasto
    """
    stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": query}],
    stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")