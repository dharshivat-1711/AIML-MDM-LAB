% Vacuum Cleaner Expert System using Prolog
% AIML Assignment 1

:- dynamic dirty/1.
:- dynamic vacuum_location/1.

% -----------------------------
% Knowledge Base: Facts
% -----------------------------

% Define rooms
room(a).
room(b).
room(c).

% Define adjacency between rooms
adjacent(a, b).
adjacent(b, a).
adjacent(b, c).
adjacent(c, b).

% Initial dirt locations
dirty(a).
dirty(c).

% Initial location of vacuum
vacuum_location(a).

% -----------------------------
% Rules: Inference Engine
% -----------------------------

% Rule 1: If the current room is dirty, action = clean
action(clean) :-
    vacuum_location(Room),
    dirty(Room).

% Rule 2: If there is a dirty adjacent room, action = move there
action(move(ToRoom)) :-
    vacuum_location(CurrentRoom),
    adjacent(CurrentRoom, ToRoom),
    dirty(ToRoom).

% Rule 3: If no dirt is present in any room, stop
action(stop) :-
    \+ dirty(_).

% -----------------------------
% Actions that change the world
% -----------------------------

% Perform cleaning: remove dirt fact
perform(clean) :-
    vacuum_location(Room),
    retract(dirty(Room)),
    format("Vacuum cleaned room ~w.~n", [Room]).

% Move to another room
perform(move(ToRoom)) :-
    retract(vacuum_location(_)),
    assert(vacuum_location(ToRoom)),
    format("Vacuum moved to room ~w.~n", [ToRoom]).

% Stop action
perform(stop) :-
    format("All rooms are clean. Stopping...~n", []).

% -----------------------------
% Recursive control loop
% -----------------------------

% Keep cleaning until all rooms are clean
start :-
    action(Action),
    perform(Action),
    Action \= stop,
    start.
