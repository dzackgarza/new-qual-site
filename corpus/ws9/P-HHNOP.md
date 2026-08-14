---
schema: qual/card@1
id: P-HHNOP
kind: problem
title: "Let $X$ and $Y$ be Banach spaces."
classification:
  areas:
  - real-analysis
  topics:
  - functional-analysis
  - compactness
relations: []
review: draft
---

::: {.problem title="?"}
Let $X$ and $Y$ be Banach spaces.
A bounded linear transformation $A:X\to Y$ is *compact* if for every bounded sequence $\{x_n\}\subseteq X$, the sequence $\{Ax_n\}$ has a convergent subsequence in $Y$.
Suppose $X$ is reflexive ($X^{**}=X$) and $X^*$ is separable.
Show that $A:X\to Y$ is compact if and only if for every bounded sequence $\{x_n\}\subseteq X$, there exists a subsequence $\{x_{n_j}\}$ and a vector $\phi\in X$ such that $x_{n_j} = \phi+r_{n_j}$ and $Ar_{n_j}\to 0$ in $Y$.
:::
