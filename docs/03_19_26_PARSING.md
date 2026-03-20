# Parsing Model

## Overview

Dub uses a positional, index-driven parsing system rather than recursive descent or grammar-based parsing.

## Key Concepts

- Source is read line-by-line.
- Operators are collected into index lists.
- Parentheses are tracked by inserting open-paren indices at position 0.
- Closing parentheses match the most recent open by popping index 0.
- No recursion, no depth tracking, no shunting yard.

## Why This Works

- The AST builder uses positional ranges.
- Operator precedence is resolved by scanning index lists.
- Parentheses define subranges without nested calls.

## Benefits

- Simpler mental model.
- No call stack overhead.
- Easy to serialize and debug.
- Naturally compatible with JSON export.
