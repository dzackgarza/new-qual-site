---
schema: qual/card@1
id: E-HAT-4.H-4
kind: exercise
title: "Dual of an iterated mapping cylinder"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

Define the dual of an iterated mapping cylinder precisely, in terms of maps from $\Delta^n$, and use this to give a definition of $\nabla X$, the dual of $\Delta X$, for $X$ a complex of spaces.

::: solution
**Goal:** Define duality on a simplex level and then apply it to an iterated simplicial cylinder.

<1> Let $\iota_n:\Delta^n\to\Delta^n$ be the order-reversing homeomorphism sending
    the vertex $e_i$ to $e_{n-i}$.
    For a map $\sigma:\Delta^n\to Z$, define its dual simplex map by
    $$
    \sigma^\vee:=\sigma\circ \iota_n:\Delta^n\to Z.
    $$

<1> For an iterated mapping cylinder of a string
    $$
    X_0\to X_1\to\cdots\to X_n,
    $$
    each cell is given by maps $\sigma_i:\Delta^i\to X_i$ with face gluing by the structure maps.
    The dual cylinder keeps the same cells and reverses every simplex map:
    each glued cell $\sigma_i$ is replaced by $\sigma_i^\vee$.
    Equivalently, on face operators one has
    $$
    d_i^\vee = d_{n-i},\qquad s_i^\vee = s_{n-i}.
    $$

<1> For a complex of spaces $X$, let $\Delta X$ be its associated simplicial space.
    Define $\nabla X$ by
    $$
    (\nabla X)_n := (\Delta X)_n,\qquad
    (d_i)_{\nabla X} = (d_{n-i})_{\Delta X},\quad
    (s_i)_{\nabla X}=(s_{n-i})_{\Delta X}.
    $$
    That is, $\nabla X$ is obtained from $\Delta X$ by replacing each simplex
    map $\sigma$ with $\sigma^\vee=\sigma\circ\iota_n$ in every degree.

Authored by **Codex 5.3 Spark Extra High**.
:::
