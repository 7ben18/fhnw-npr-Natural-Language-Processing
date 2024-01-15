# Few Shot LLM

Hier in diesem Ordner befinden sich der Few-Shot Approach mittels dem Large Language Model Phi-2 und GPT-2. 

## Daten

Wir nutzen hier die Immobilienchallenge Daten, welche wir im HS22 erhalten haben und versuchen mit dem Few-Shot Approach die gewünschten Immobilien zu finden.

## Few-Shot Approach

Der Few-Shot Approach basiert auf der Idee, dass ein Modell in der Lage sein sollte, allgemeine Muster und Zusammenhänge aus einer begrenzten Anzahl von Beispielen zu lernen und dann diese Muster auf neue, ähnliche Aufgaben anzuwenden. In unserem Beispiel haben wir Beispiel Sätze, welche wir dem Modell geben um die gewünschten Immobilien zu finden. 

### Few-shot Beispiel
```python
few_shot_examples = [
    {
        "Question": "I am looking for an flat in Zurich under 1'000'000 CHF.", 
        "Answer": "Here are some options for apartments in Zurich under 1'000'000 CHF: (max_price = 1000000, location_keyword = Zürich, property_type = flat)"
    }
]
```

## Use-Case

In unserem Use-Case versuchen wir einen mittels Few-Shot Approaches bei Language Models die gewünschten Immobilien zu finden. Dabei erhalten wir durch die Eingabe von Simplen Sätzen, wie zum Beispiel: "Ich suche eine Wohnung in Zürich, welche 3 Zimmer hat und nicht mehr als 1000000 Franken kostet", ein DataFrame zurück mit den gewünschten Immobilien.


## Phi-2 Modell

Das [Phi-2 Modell](https://huggingface.co/microsoft/phi-2) wurde von Microsoft entwickelt und ist ein relativ kleines Large Language Modell (SML). Phi-2 ist ein Transformer mit 2.7 Milliarden Parametern. Es wurde unteranderem mit synthetischen Daten trainiert und ist für den Einsatz für Forschungszwecken, Question-Answering und Chat Format gedacht. 


## GPT-2 Modell

Das [GPT-2-Modell](https://huggingface.co/gpt2) wurde erstmals im Februar 2019 von OpenAI veröffentlicht. Die Grundlage des GPT-2-Modells ist der Transformer-Algorithmus, der für sein effizientes Handling von Sequenzen bekannt ist. Dieser Algorithmus ermöglicht es dem Modell, lange Texte zu analysieren und anschliessend Texte von hoher Qualität zu generieren. GPT-2 wurde durch eine grosse Menge an englischen Textdaten trainiert. 

## TinyLlama Chat

[TinyLlama Chat](https://huggingface.co/TinyLlama/TinyLlama-1.1B-step-50K-105b) ist eine kleinere Variante von Llama 2, welches 1.1 Milliarden Parameter hat. 

## Fazit

Das Fazit wurde im Übergeordneten Ordner im [README](../README.md) geschrieben. 
