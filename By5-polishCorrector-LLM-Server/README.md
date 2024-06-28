---
license: lgpl
pipeline_tag: text2text-generation
language:
- be
- da
- de
- el
- en
- es
- fr
- it
- nl
- pl
- pt
- ro
- ru
- sk
- sv
- uk
---

# ByT5-text-correction

A small multilingual utility model intended for simple text correction. It is designed to improve the quality of texts from the web, often lacking punctuation or proper word capitalization. The model was trained to perform three types of corrections:
* Restoring punctuation in sentences.
* Restoring word capitalization.
* Restoring diacritical marks for languages that include them.

The following languages are supported: Belarusian (be), Danish (da), German (de), Greek (el), English (en), Spanish (es), French (fr), Italian (it), Dutch (nl), Polish (pl), Portuguese (pt), Romanian (ro), Russian (ru), Slovak (sk), Swedish (sv), Ukrainian (uk).

The model takes as input a sentence preceded by a language code prefix. For example:

```python
from transformers import pipeline
generator = pipeline("text2text-generation", model="sdadas/byt5-text-correction")
sentences = [
    "<pl> ciekaw jestem na co licza onuce stawiajace na sykulskiego w nadziei na zwrot ku rosji",
    "<de> die frage die sich die europäer stellen müssen lautet ist es in unserem interesse die krise auf taiwan zu beschleunigen",
    "<ru> при своём рождении 26 августа 1910 года тереза получила имя агнес бояджиу"
]
generator(sentences, max_length=512)
# Ciekaw jestem na co liczą onuce stawiające na Sykulskiego w nadziei na zwrot ku Rosji.
# Die Frage, die sich die Europäer stellen müssen, lautet: Ist es in unserem Interesse, die Krise auf Taiwan zu beschleunigen?
# При своём рождении 26 августа 1910 года Тереза получила имя Агнес Бояджиу.
```