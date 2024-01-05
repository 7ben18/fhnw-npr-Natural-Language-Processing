# Few Shot LLM

Hier in diesem Ordner befinden sich der Few-Shot Approach mittels dem Large Language Model Phi-2 und GPT-2. 

## Daten

Wir nutzen hier die Immobilienchallenge Daten, welche wir im HS22 erhalten haben und versuchen mittels dem Few-Shot Approach die gewünschten Immobilien zu finden.


## Phi-2 Modell

Das [Phi-2 Modell](https://huggingface.co/microsoft/phi-2) wurde von Microsoft entwickelt und ist ein relativ kleines Large Language Modell (SML). Phi-2 ist ein Transformer mit 2.7 Milliarden Parametern. Es wurde unteranderem mit synthetischen Daten trainiert und ist für den Einsatz für Forschungszwecken, Question-Answering und Chat Format gedacht. In unserem Use-Case versuchen wir einen mittels Few-Shot Approaches die gewünschten Immobilien zu finden. Dabei erhalten wir durch die Eingabe von Simplen Sätzen, wie zum Beispiel: Ich suche eine Wohnung in Zürich, welche 3 Zimmer hat und nicht mehr als 1000000 Franken kostet. Die gewünschten Immobilien als Dataframe zurück.


## GPT-2 Modell

Das GPT-2-Modell wurde erstmals im Februar 2019 von OpenAI veröffentlicht. Die Grundlage des GPT-2-Modells ist der Transformer-Algorithmus, der für sein effizientes Handling von Sequenzen bekannt ist. Dieser Algorithmus ermöglicht es dem Modell, lange Texte zu analysieren und anschließend Texte von hoher Qualität zu generieren.