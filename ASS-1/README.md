# Vacuum Cleaner Expert System using Prolog

## AIML Assignment 1

### Aim
To design and implement a simple Vacuum Cleaner Expert System using Prolog that can identify dirty rooms, decide appropriate cleaning or movement actions using rules, and automatically clean all dirty rooms through an inference engine.

## Technology Used
- Programming Language: Prolog
- Platform/IDE: SWI-Prolog / SWISH
- Main Concepts: Facts, Rules, Inference Engine, Dynamic Predicates, Recursion

## Files
- `vacuum_cleaner.pl` — Complete Prolog source code
- `README.md` — Project description and instructions
- `sample_output.txt` — Sample queries and output

## How to Run

### Using SWISH
1. Open SWISH (SWI-Prolog online environment).
2. Create a new Prolog program.
3. Copy the contents of `vacuum_cleaner.pl`.
4. Run the queries given below.

### Using SWI-Prolog
1. Install SWI-Prolog.
2. Open the terminal.
3. Load the file:
   `[vacuum_cleaner].`
4. Execute the required queries.

## Example Queries

```prolog
room(X).
adjacent(X, Y).
dirty(X).
vacuum_location(X).
action(X).
perform(clean).
perform(move(c)).
start.
```

## Expected Result

The expert system identifies dirty rooms, cleans the current dirty room, moves to an adjacent dirty room when required, and stops after all rooms are clean.

Typical execution:

```text
Vacuum cleaned room a.
Vacuum moved to room c.
Vacuum cleaned room c.
All rooms are clean. Stopping...
true.
```

## Working Principle

The program stores room information and the initial dirty-room and vacuum-location facts. The inference rules determine whether the vacuum should clean the current room, move to an adjacent dirty room, or stop when no dirty rooms remain. The `start` predicate repeatedly performs the selected action until the stopping condition is reached.
