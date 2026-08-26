# AIML Assignment 1.2 - Country Chatbot

## Aim
To design and implement a simple rule-based Country Chatbot using SWI-Prolog that provides information about countries based on user queries.

## Countries Supported
- India
- Japan
- France
- USA
- Australia

## Information Provided
The chatbot can provide:
- Capital
- Currency
- Continent

## Technology
- Programming Language: Prolog
- IDE / Platform: SWISH / SWI-Prolog
- No external dataset or external packages are required.

## How to Run
1. Open SWISH or SWI-Prolog.
2. Load `country_chatbot.pl`.
3. Run:
   `chat.`
4. Enter questions containing a supported country and the requested information.
5. Type `quit` to exit.

## Direct Test Queries
```prolog
respond(["india","currency"]).
respond(["france","continent"]).
respond(["usa","capital"]).
respond(["australia","currency"]).
respond(["japan","capital"]).
```

## Expected Responses
- India currency: Rupee
- France continent: Europe
- USA capital: Washington DC
- Australia currency: Australian Dollar
- Japan capital: Tokyo
