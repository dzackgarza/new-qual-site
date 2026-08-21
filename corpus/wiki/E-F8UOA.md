---
schema: qual/card@1
id: E-F8UOA
kind: exercise
title: Continuity sets are G-delta; no function continuous exactly on the rationals
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §48.7"}

Prove the following.

Theorem.
If $D$ is a countable dense subset of $\mathbb{R}$, there is no function $f: \mathbb{R} \to \mathbb{R}$ that is continuous precisely at the points of $D$.

(a) Show that if $f: \mathbb{R} \to \mathbb{R}$, then the set $C$ of points at which $f$ is continuous is a $G_\delta$ set in $\mathbb{R}$.
[Hint: Let $U_n$ be the union of all open sets $U$ of $\mathbb{R}$ such that $\operatorname{diam} f(U) < 1/n$. Show that $C = \bigcap U_n$.]

(b) Show that $D$ is not a $G_\delta$ set in $\mathbb{R}$.
[Hint: Suppose $D = \bigcap W_n$, where $W_n$ is open in $\mathbb{R}$. For $d \in D$, set $V_d = \mathbb{R} - \ts{d}$. Show $W_n$ and $V_d$ are dense in $\mathbb{R}$.]
:::
