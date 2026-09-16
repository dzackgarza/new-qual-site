---
schema: qual/card@1
id: D-MMDM3
kind: definition
title: Attaching an $n$-cell
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $n\geq 0$.
Let $D^n\subseteq\RR^n$ be the closed unit ball and $S^{n-1}=\del D^n$ its boundary sphere, with $S^{-1}=\emptyset$.
For a continuous map $f\colon S^{n-1}\to X$, the space obtained by \dfn{attaching an $n$-cell} to $X$ along $f$ is the quotient space
$$
X\cup_f D^n \coloneqq \qty{X\disjoint D^n}/\qty{s\sim f(s) \text{ for } s\in S^{n-1}},
$$
the case $X_0=X$, $X_1=D^n$, $A=S^{n-1}$ of [[D-HRU62|attaching a space along a map]].
The map $f$ is the \dfn{attaching map}.
The composite $\Phi\colon D^n\to X\disjoint D^n\to X\cup_f D^n$ of the inclusion and the quotient map is the \dfn{characteristic map}, its image $\Phi(D^n)$ is the \dfn{closed $n$-cell}, and $e^n\coloneqq\Phi(D^n\setminus S^{n-1})$ is the \dfn{open $n$-cell}.
:::

::: {.example}
In low dimensions:

- $n=0$: $D^0$ is a point and $S^{-1}=\emptyset$, so $X\cup_f D^0=X\disjoint\ts{\pt}$.

- $n=1$: $D^1=[-1,1]\subseteq\RR$ and $f$ is a map $S^0=\ts{-1,1}\to X$; the closed $1$-cell is the image of a path from $f(-1)$ to $f(1)$.

- $n=2$: $D^2\subseteq\RR^2$ is the closed disk, attached along a map $S^1\to X$.

- $n=3$: $D^3\subseteq\RR^3$ is the closed ball, attached along a map $S^2\to X$.
:::
