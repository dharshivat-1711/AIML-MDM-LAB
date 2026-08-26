% =========================================
% COUNTRY CHATBOT USING PROLOG
% =========================================

chat :-
    writeln("===== COUNTRY CHATBOT ====="),
    writeln("Ask about India, Japan, France, USA, or Australia."),
    writeln("You can ask about capital, currency, or continent."),
    writeln("Type quit to exit."),
    nl,
    repeat,
    write("You: "),
    read_line_to_string(user_input, Input),
    string_lower(Input, Lower),
    split_string(Lower, " ", "?!.,", Words),
    (
        member("quit", Words)
        ->
        writeln("Bot: Goodbye!"),
        !
        ;
        respond(Words),
        fail
    ).

% INDIA
respond(Words) :-
    member("india", Words),
    (
        member("capital", Words)
        ->
        writeln("Bot: The capital of India is New Delhi.")
        ;
        member("currency", Words)
        ->
        writeln("Bot: The currency of India is the Rupee.")
        ;
        member("continent", Words)
        ->
        writeln("Bot: India is in Asia.")
        ;
        writeln("Bot: India is a country in South Asia.")
    ),
    !.

% JAPAN
respond(Words) :-
    member("japan", Words),
    (
        member("capital", Words)
        ->
        writeln("Bot: The capital of Japan is Tokyo.")
        ;
        member("currency", Words)
        ->
        writeln("Bot: The currency of Japan is the Yen.")
        ;
        member("continent", Words)
        ->
        writeln("Bot: Japan is in Asia.")
        ;
        writeln("Bot: Japan is an island country in East Asia.")
    ),
    !.

% FRANCE
respond(Words) :-
    member("france", Words),
    (
        member("capital", Words)
        ->
        writeln("Bot: The capital of France is Paris.")
        ;
        member("currency", Words)
        ->
        writeln("Bot: The currency of France is the Euro.")
        ;
        member("continent", Words)
        ->
        writeln("Bot: France is in Europe.")
        ;
        writeln("Bot: France is a country in Europe.")
    ),
    !.

% USA
respond(Words) :-
    member("usa", Words),
    (
        member("capital", Words)
        ->
        writeln("Bot: The capital of USA is Washington DC.")
        ;
        member("currency", Words)
        ->
        writeln("Bot: The currency of USA is the US Dollar.")
        ;
        member("continent", Words)
        ->
        writeln("Bot: USA is in North America.")
        ;
        writeln("Bot: USA is a country in North America.")
    ),
    !.

% AUSTRALIA
respond(Words) :-
    member("australia", Words),
    (
        member("capital", Words)
        ->
        writeln("Bot: The capital of Australia is Canberra.")
        ;
        member("currency", Words)
        ->
        writeln("Bot: The currency of Australia is the Australian Dollar.")
        ;
        member("continent", Words)
        ->
        writeln("Bot: Australia is in Oceania.")
        ;
        writeln("Bot: Australia is a country and continent.")
    ),
    !.

% DEFAULT RESPONSE
respond(_) :-
    writeln("Bot: Sorry, I do not have information about that country.").
