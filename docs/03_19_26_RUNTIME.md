# Runtime Execution Model

## Short-Term Plan

- Execute AST directly in Python.
- Use Python classes to simulate:
  - DubObject
  - DubFunction
  - DubClass
  - DubList
  - DubDict
  - Scopes and environments

## Why Python First

- Fast iteration.
- Easy to experiment with semantics.
- No need to commit to a final architecture early.
- Lets the language "find itself" before optimization.

## Long-Term Options

- Build a bytecode VM.
- Write a C-based interpreter.
- Compile AST to C.
- Add JIT compilation later.

## Execution Pipeline

1. Read source text.
2. Parse into positional AST.
3. Walk AST and evaluate nodes.
4. Manage scopes, variables, and functions.
