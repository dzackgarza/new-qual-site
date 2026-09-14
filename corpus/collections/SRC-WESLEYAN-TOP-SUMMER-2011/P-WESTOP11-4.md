---
schema: qual/card@1
id: P-WESTOP11-4
kind: problem
title: Maximal ideals of rings of continuous functions on compact Hausdorff spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
For a topological space $X$, let $C(X)$ be the ring of continuous real-valued functions on $X$. For $f\in C(X)$ and $S\subseteq X$, define
\[
Z(f)=\{p\in X:f(p)=0\},
\qquad
I(S)=\{f\in C(X):S\subseteq Z(f)\}.
\]

1. Show that $I(S)$ is an ideal of $C(X)$, that
   \[
   I(S)=I(\overline S),
   \]
   and that $S_1\subseteq S_2$ implies $I(S_2)\subseteq I(S_1)$.
2. If $X$ is completely regular and $p\in X$, show that $I(\{p\})$ is a maximal ideal of $C(X)$.
3. If $X$ is compact Hausdorff and $I$ is a maximal ideal of $C(X)$, show that
   \[
   I=I(\{p\})
   \]
   for some $p\in X$.
:::
