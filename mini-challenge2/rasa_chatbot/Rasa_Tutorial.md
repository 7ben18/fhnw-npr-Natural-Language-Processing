# RASA Overview

Rasa is a framework to build custom chatbots easier

# State Machines vs. Neural Methods

## Understanding Text

### Rule Based

- A regualr expression that finds and extracts email addresses 
- dont need much data
- can run fast
- BUT they are not good at handing things they have never seen before

### Neural approaches

- Transformer based model Sort text into intents based on examples its been provided
- Require training examples
- BUT they are good at hadnlings things they have never seen before, making "informed guesses"

### Rasa Assisent
Rasa might use both

## Deciding what to do next
Dialog Policy -> Given the conversation so far, what should the assistant do or say next?

### Rule based
- A big tree of all possible paths of a conversation that can take place (state Machine)
- Tradination approach
- BUT can not ahndle digressions (complex paths)

### Neural approaches
- based on transformer, picks the next best turn based on the conversation it has seen so far
- BUT this approach lets user have more natural conversations even if they say something different oder. 

## How to make sure conversations work and improve over time

### The Rasa approach is
- Flexible, every conversation might be unique
- works better the more high quality training data we have

### How do you make sure conversations work?
- Manually reviewing and annotating conversations

### How do you make sure conversations improve over time?
- Correct any errors your assisant made in a conversation, then add training data for retrain and redeploy


# Rasa Setup

create an environment (venv or conda) and install rasa

afterwards create in the cmd rasa

```bash
rasa init
```

everthing yes until you can chat with the bot, its generating files and folders and training a simple model as well. 

following folders are created by rasa init 

- actions 
- data 
- nlu.yml (intent and entities)
- stories.yml (potential conversation flow)
- rules.yml (conditional rules, exmaple goodbye)
- models (if training yes)
- tests
- config.yml (config for the model)
- credentials.yml
- domain.yml (All the things your assistant can say and do)
- endpoints.yml

command lines 

# rasa commands

help command
    
```bash
rasa -h
```

init command 

```bash
rasa init -h
```

train command

```bash
rasa train -h
```

talk to assistant bot 

```bash
rasa shell
```

debug flag, shows more information on the issues

```bash
rasa shell --debug
```

# domain.yml in details

domain contents: 

- Response (These are things the assisant can say to users)
- Intents (These are categories of things users say)
- Slots (thee are variables remebered over the course of a conversation)
- Entities (These are specific pieces of information the assistant should extract from the user's messages)
- Forms and Actions (These are things the assistant can do)

## Responses

```yml
responses:
  utter_greet:
    - text: "Hey! {name}. How are you?"
    - text: "Hey! How are you {name}?"
  utter_cheer_up:
    - text: "Here is something to cheer you up:"
      image: "https://i.imgur.com/nGF1K8f.jpg"
  utter_did_that_help:
    - text: "Did that help you?"
  utter_happy:
    - text: "Great carry on!"
    buttons:
        - title: "Great"
            payload: "great"
        - title: "Not great"
            payload: "not great"
  utter_goodbye:
    - text: "Bye"
  utter_ask_game:
    - text: "What game do you want to play?"
      channel: "slack"
    - text: "What game do you want to play?"
  utter_book_time:
    - custom:
        blocks:
        - type: section
            text:
            type: mrkdwn
            text: "Pick a date for your appointment:"
            type: mrkdwn
        accessory:
            type: static_select
            placeholder:
            type: plain_text
            text: "Select a date"
            options:
            - text:
                type: plain_text
                text: "Today"
                emoji: true
                value: "value-0"
            - text:
                type: plain_text
                text: "Tomorrow"
                emoji: true
                value: "value-1"
            - text:
                type: plain_text
                text: "August 10th"
                emoji: true
                value: "value-2"
```

## Intents

Classes for multiclass classifcation!

```yml
intents:
  - greet
  - goodbye
  - affirm
  - deny
  - mood_great
  - mood_unhappy
  - bot_challenge
  - ask_game
  - book_time
  - how_to_play
  - how_to_get_started
```

# data 

- there are two types of data
the text data used to pretrain any models or features that are used. (language models, word embeddings etc..)

- user generated text

- patterns of conversations

- examples
    - customer support logs
    - User conversations with you assistant! 


# Stories
training data to teach you assistant what it should do next! 
(memory of the conversation)

If the assisant hasnt seen the converation before it guesses what the most likely next action is depending on threshold. 

if you have conversational data:
    - if you have conversations start, with those patterns!

Generating your own conversational patterns:
    - its easiest to use interactive learning to create stories
    - start with common flows (happy path)
    - then add in more complex flows (digressions, errors, etc..)

Once your model is trained
    - you can use the interactive learning to correct any mistakes your assistant makes
    - you can use the interactive learning to add more examples to your training data

rasa-projekt/data/stories.yml

intent -> what the model detected
actions -> what the model is doing 

```yml
stories:
- story: happy path
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_great
  - action: utter_happy
  - intent: mood_unhappy
  - action: utter_cheer_up
  - action: utter_did_that_help
  - intent: affirm
  - action: utter_happy
```

Or conditional stories

```yml
- story: newsletter signup with OR
    steps:
    - intent: signup_newsletter
    - action: utter_ask_contact_signup
    - or:
        - intent: affirm
        - intent: thanks
    - action: action_signup_newsletter
```

with checkpoints
checkpoints can be used to start new stories from a certain point
    
```yml
- story: happy path with checkpoints
    steps:
    - intent: greet
    - action: utter_greet
    - intent: mood_great
    - action: utter_happy
    - checkpoint: happy_path_check
    - intent: mood_unhappy
    - action: utter_cheer_up
    - action: utter_did_that_help
    - intent: affirm
    - action: utter_happy
```

# Rules

- a way to describe short pieces of conversations that always go the same way

rasa-projekt/data/rules.yml

```yml
rules:
- rule: Say goodbye anytime the user says goodbye
  steps:
  - intent: goodbye
  - action: utter_goodbye
```

DO: 
- use actual user conversations as stories
- have small stories that arent full conversations
- use rules for one-off interactions (checking balance, check if a bot?)

DONT:
- use rules for multi-turn onteractions
- use OR statements and checkpoints often
- wirte out every possible conversation path
- delay user testing

# NLU

rasa-projekt/data/nlu.yml

intents for multi class classification

input data will be assigned to the intent with the highest confidence score

```yml
nlu:
- intent: greet
  examples: |
    - hey
    - hello
    - hi
    - hello there
    - good morning
    - good evening
    - moin
    - hey there
    - let's go
    - hey dude
    - goodmorning
    - goodevening
    - good afternoon
    - yo
    - hey ya
    - hi folks
    - hello everybody
```

if you have data, 
- modified content analysis
    - Go through data point by hand and assign each datapoint
    - if no existing group fits, add a new one
    - at given intervals go thourhg the data and reassign any misclassified data

- cant you just automate this?
    - its easiest to use interactive learnint to create stories
    - start with common flows (happy path)
    - then add in more complex flows (digressions, errors, etc..)

- no data?
    - start with most common intent
    - most people want to do the same thing 
    - use the experts in uour institution to help you

- helpful
    - start with the smallest possible number of intents (cover your use case)


# why fewer intents?

older style of conversational design
RASA style CDD -> only need to start with the most popular important intents & a way to handle things outside them
Continue to build from there if thats what users need
Human reasons, the more intents the more training data, maintance, documentation
more intents = annotation more diffucult
ML reasons
Transformer classifier sclae linearly with the n of classes
entity extraction (with very lightweiht rule-based systems like Duckling) is often faster

# Pairing down intents

Dont use intents as a way to store information

Do a lot of the same tokens show up in training data for two intents? Consider if they can be combiend

```yml
book_train:
    One train ticket
    Need to book a trai ride
    A rail journey please

book_plane:
    One plane ticket
    Need to book a plane ride
    A flight please
```

combine them into one intent
    
```yml
book_travel:
    One train ticket
    Need to book a trai ride
    A rail journey please
    One plane ticket
    Need to book a plane ride
    A flight please
```

# Training Data

ambigous = mehrdeutig

- user generated > synthetic
- each utterance should unambiguous match to a single intent
- is an utterance ambiguous? 

