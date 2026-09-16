---
schema: qual/card@1
id: P-PRACT20-W5-35
kind: problem
title: Entire functions of linear growth are linear polynomials
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 35).
---

::: {.problem}
Suppose that $f : \CC \to \CC$ is an entire function such that $\abs{f(z)} \leq C\abs{z}$ for all $z$ sufficienty large. Prove that $f(z) = c_1 + c_2 z$ for some constants $c_1, c_2$. [Note: this is a generalization of Liouville’s Theorem. It can actually be generalized further: if $f$ is entire and $\abs{f(z)} \leq C\abs{z}^n$ for sufficiently large $z$, then $f$ is a polynomial of degree $\leq n$.]
:::
