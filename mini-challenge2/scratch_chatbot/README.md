# Scatch Chatbot

Hier in diesem Folder befinden sich die Dateien, welche für die Entwicklung des Chatbots verwendet wurden.

## Beschreibung

Nachdem wir uns mit der RASA Chatbot Software mehrere Stunden auseinandergesetzt haben und auf viele Probleme gestossen sind, haben wir uns entschieden, einen Chatbot von Grund auf selber zu entwickeln. Dieser Chatbot ist in Python geschrieben und verwendet die gängigsten Bibliotheken für die Erstellung von Chatbots.

Mit RASA konnten wir uns nicht anfreunden, `yml` Files debugen und konfigurieren sowie den Befehl `rasa train`, welches im Hintergrund ein Model trainiert, welches wir nicht sehen können, hat uns nicht gefallen. Wir wollten einen Chatbot, welcher wir selber debugen können und welcher wir selber trainieren können erstellen, aus diesem Grund haben wir uns für einen eigenen Chatbot entschieden.

## Use Case

Die Chatbots sind in der Lage die neusten News aus dem Internet zu scrapen und diesem dem User zurückzugeben. Der User kann den Chatbot nach den neusten News fragen und der Chatbot wird diese News zurückgeben, welche im Datenset hinterlegt ist.

## Dateien

Die Hauptnotebooks für den ChatBot sind:

| Notebook | Beschreibung |
| --- | --- |
| `scratch_news_bot_V1.ipynb` | Notebook für den Scratch Bot `Stupid Bounty Hunter Bot` <br> Im Hintergrund ist ein neuronales Netz, welches eine Intent Klassifikation durchführt. |
| `scratch_news_bot_V2.ipynb` | Notebook für den Scratch Bot `Todays News Assisstent Bot` <br> Im Hintergrund befindet sich ein Transformer Modell|


In src befinden sich die Python Files, welche für die Entwicklung des Chatbots verwendet wurden.

| Python File | Beschreibung |
| --- | --- |
| `neuralmodel.py` | Beinhaltet das Neurale Netz für den Scratchbot Stupid Bounty Hunter Bot. |
| `preprocessing.py` | Beinhaltet die Simple Preprocessing Funktionen für die Textdaten für den Stupid Bounty Hunter Bot. |
| `news_scraper.py` | Beinhaltet den News Scraper, welcher die News von der Website `https://www.srf.ch` scrapet. |

Im Folder notebooks befinden sich Notebooks für die Entwicklung des Chatbots, bzw Experimente mit dem Chatbot.

# Infos

Dieser Scratch Bot wurde im Rahmen des Moduls Natural Language Processing an der Fachhochschule Nordwestschweiz entwickelt.