from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")

async def translate(text, source, target):
    input_text = f"Translate {source} to {target}: {text}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids)
    return tokenizer.decode(output[0], skip_special_tokens=True)