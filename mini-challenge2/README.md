# npr Mini-Challenge 2

Hier in diesem Repository befindet sich unsere npr Mini-Challenge 2 Abgabe, welche von Yannic Lais, Rami Taribishi und Si Ben Tran im HS23 an der FHNW bearbeitet wurde. 

## Aufgabenstellung aus dem Spaces
Mini-Challenge 2-C (LE6): Chatbot

You build a simple chatbot for hotel recommendation (here you can combine with npr and webscraping challenge) or extend the chatbot from the library (auxilio, please take contact with me), with rasa or dialogflow. You can also propose a use case. Important is the way intent are recognized and NER or variables are extracted. Delivery is a report on the use case, interactions and how intents are recognized and variables extracted. Also an error analysis on concrete conversations (confidence of models, explanation of predictions, etc.) should be undertaken. The submission can be done in a group of 2 or 3.

## Aufbau des Repositories

Dieses Repository beinhaltet hauptsächlich drei Ordner, mit denen wir jeweils versucht haben die Aufgabenstellung Mini-Challenge 2-C zu lösen. Zu jedem Ordner befindet sich ein README.md, welches kurz beschreibt, was wir erarbeitet haben.

| Ordner | Beschreibung |
| --- | --- |
| `few_shot_llm` | Hier befindet sich unser Ansatz mit dem Few-Short Small Language Model Phi-2, GPT-2 und TinyLlama Chat |
| `rasa_chatbot` | Hier befindet sich unser erseter Ansatz mit dem RASA Chatbot |
| `scratch_chatbot` | Hier befindet sich ein anderer Chatbot Ansatz, welche versucht wurde von Grundauf zu erstellen |


## Fazit

### Few-Shot Approach

#### Phi-2 Modell
Unser erster Few-Shot Approach mit dem Phi-2 Modell hat gut funktioniert. Das Phi-2 Modell kann mit wenig Beispielen sehr gut umgehen und liefert gute Resultate. Es versteht auch, wenn in der Anfrage ein anderer Intent sich in der Query befindet und kann diesen auch richtig zuordnen. Bsp: Ob es sich um eine Immobilienanfrage handelt oder etwas anderes wie, ob er Brot hat. Auch Anfragen auf Deutsch kann unser Phi-2 Modell verstehen. Wir sind erstaunt, dass die Implementierung relativ einfach war sowie der Few-Shot Approach gute erste Resultate lieferte. Named Entity Recogination von Städtennamen erkennt das Modell, jedoch funktioniert der Wert der Immobilien nicht. Es versteht nicht, wenn wir einen gewissen Preisbereich angeben wollen. 

#### GPT-2 Modell
Das GPT-2 Modell mit dem Few-Shot Approach analog wie beim Phi-2 Modell funktionierte nur bedingt. Die gleichen Queries, wie beim Phi-2 Modell wurden verwendet, um beide Modelle miteinander zu vergleichen. GPT-2 gibt Antworten zurück, jedoch sind diese nicht richtig geschrieben oder haben die Falsche Eigenschaften. Die Struktur jeweils ist die richtige, jedoch sind die Werte falsch.
Wir haben erkannt, dass das GPT-2 Modelle nicht so gut Zahlen interepretieren kann, welches getrennt werden durch einen Apostroph. Bsp: 1'000'000.00. 

#### TinyLlama Chat
TinyLlama Chat hat unserer Meinung nach am besten performt. Es konnte aus dem Few-Shot Approach lernen und versteht auch, wenn wir Immobilienanfragen schreiben die einen Preisbereich abdecken und gibt auch entsprechend die richtigen Antworten zurück. Auch erstaunt hat uns die Tatsache, dass TinyLlama Chat auch auf Deutsch funktionierte. Es versteht die Anfragen und kann diese auch richtig zuordnen. Was uns aufgefallen ist, ist dass TinyLlama Chat durch den Few-Shot Approach der Struktur der Anfrage folgt, unabhängig was für einen Intent gefragt wird. So kann es Bsp. nicht verstehen ob es sich um eine Immobilienanfrage handelt oder um eine Anfrage, ob er Brot hat, und versucht daraus immer eine Immobilienanfrage zu machen. 

### RASA Chatbot

Der Rasa ChatBot hat uns sehr viel Zeit gekostet. Wir haben uns sehr viel Zeit damit verbracht, die yml Files zu debuggen. Nach einer gewissen Zeit haben wir uns dann entschieden, einen Chatbot von Grund auf selber zu entwickeln. Das ist dann der Grund auch, warum `scratch_chatbot` entstanden ist. Resultate vom Rasa Chatbot sind nicht vorhanden. 

### Scratch Chatbot

Der Scratch Chatbot webscrapt die aktuellen Tagesnews und ist ein regelbasierter Chatbot der auf die Anfragen der User antwortet. Der Scratch Bot klassifiziert aufgrund der Anfrage den jeweiligen Intent und gibt dann diese dann als Antwort zurück. 