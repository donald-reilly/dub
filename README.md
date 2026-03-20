# Dub Language

Dub is an experimental programming language built from first principles with a focus on clarity, simplicity, and a unique execution model. It is not based on traditional compiler theory or parser generators — instead, Dub grows organically through experimentation, iteration, and a deep curiosity about how languages work under the hood.

Dub is currently in early development, but the foundations are already forming:

- a positional, index-driven parser  
- a non-recursive AST  
- JSON-serializable intermediate representation  
- a Python-based runtime for rapid experimentation  

This repository tracks the evolution of Dub’s design, architecture, and supporting tools.

---

## 🌱 Philosophy

Dub is built on a few core ideas:

- **First principles over tradition**  
  No recursive descent, no shunting yard, no grammar tables.  
  Dub’s parser is built around positional indices and operator ranges.

- **AST-first architecture**  
  The AST is the heart of the language.  
  Everything else — runtime, bytecode, VM — grows from it.

- **Portability through JSON**  
  The AST is fully serializable, making it easy to execute in Python, C, Rust, or a future Dub VM.

- **Iterative, curiosity-driven development**  
  Dub evolves through cycles of experimentation, stepping away, learning from other projects, and returning with clarity.

---

## 🔍 Project Structure

This repository is organized into several design documents:

- **[`DESIGN.md`](./DESIGN.md)** — High-level overview of the language’s goals and architecture.
- **[`PARSING.md`](./PARSING.md)** — Details of the positional, index-driven parsing model.
- **[`AST.md`](./AST.md)** — Structure, philosophy, and long-term vision for the AST.
- **[`RUNTIME.md`](./RUNTIME.md)** — Execution model, Python runtime, and future VM plans.
- **[`ROADMAP.md`](./ROADMAP.md)** — Development phases and long-term milestones.
- **[`NOTES.md`](./NOTES.md)** — Personal development notes and design reflections.

These documents evolve alongside the language itself.

---

## ⚙️ Current Status

Dub is in **Phase 1** of development:

- Parsing basic expressions  
- Building a positional AST  
- Exporting AST to JSON  
- Experimenting with Python-based execution  

The goal of this phase is to establish a solid foundation before moving into runtime design or bytecode.

---

## 🔄 Supporting Projects

Several companion projects help shape Dub’s development:

- **BInspected** — Tools for runtime introspection and recursion control.
- **FigMan** — Being split into:
  - `FigConfig` for configuration management  
  - `FigAST` for AST utilities  
- **DesignMe** — A project focused on finishing, polishing, and publishing a complete tool.

Each project strengthens a different part of the skill set needed to build Dub.

---

## 🎯 Long-Term Vision

Dub aims to grow into:

- A language with a unique parsing and execution model  
- A portable AST-based architecture  
- A bytecode VM or C-based interpreter  
- A self-hosting system capable of compiling itself  

This is a long-term, multi-year journey — and this repository documents every step.

---

## 📬 Contributing

Dub is currently a personal experimental project, but feedback, ideas, and discussions are welcome.  
As the language matures, contribution guidelines will be added.

---

## 📜 License

To be determined.
