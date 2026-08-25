---
schema: qual/card@1
id: E-PQHZN
kind: exercise
title: The long line
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Connectedness
relations: []
review: draft
---

::: {.exercise title="Munkres §24.12"}

Recall that $S_\Omega$ denotes the minimal uncountable well-ordered set.
Let $L$ denote the ordered set $S_\Omega \times [0, 1)$ in the dictionary order, with its smallest element deleted.
The set $L$ is a classical example in topology called the long line.

Theorem.
The long line is path connected and locally homeomorphic to $\mathbb{R}$, but it cannot be imbedded in $\mathbb{R}$.

(a) Let $X$ be an ordered set; let $a < b < c$ be points of $X$.
Show that $[a, c)$ has the order type of $[0, 1)$ if and only if both $[a, b)$ and $[b, c)$ have the order type of $[0, 1)$.

(b) Let $X$ be an ordered set.
Let $x_0 < x_1 < \cdots$ be an increasing sequence of points of $X$; suppose $b = \sup\ts{x_i}$.
Show that $[x_0, b)$ has the order type of $[0, 1)$ if and only if each interval $[x_i, x_{i+1})$ has the order type of $[0, 1)$.

(c) Let $a_0$ denote the smallest element of $S_\Omega$.
For each element $a$ of $S_\Omega$ different from $a_0$, show that the interval $[a_0 \times 0, a \times 0)$ of $S_\Omega \times [0, 1)$ has the order type of $[0, 1)$.
[Hint: Proceed by transfinite induction. Either $a$ has an immediate predecessor in $S_\Omega$, or there is an increasing sequence $a_i$ in $S_\Omega$ with $a = \sup\ts{a_i}$.]

(d) Show that $L$ is path connected.

(e) Show that every point of $L$ has a neighborhood homeomorphic with an open interval in $\mathbb{R}$.

(f) Show that $L$ cannot be imbedded in $\mathbb{R}$, or indeed in $\mathbb{R}^n$ for any $n$.
[Hint: Any subspace of $\mathbb{R}^n$ has a countable basis for its topology.]
:::
