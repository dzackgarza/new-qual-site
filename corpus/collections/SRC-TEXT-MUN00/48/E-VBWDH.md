---
schema: qual/card@1
id: E-VBWDH
kind: problem
title: Uniform boundedness principle
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
---

::: {.exercise}

Prove the following.

Theorem (Uniform boundedness principle).
Let $X$ be a complete metric space, and let $\mathcal{F}$ be a subset of $\mathcal{C}(X, \mathbb{R})$ such that for each $a \in X$, the set

$$
\mathcal{F}_a = \ts{f(a) \mid f \in \mathcal{F}}
$$

is bounded.
Then there is a nonempty open set $U$ of $X$ on which the functions in $\mathcal{F}$ are uniformly bounded, that is, there is a number $M$ such that $\abs{f(x)} \leq M$ for all $x \in U$ and all $f \in \mathcal{F}$.
[Hint: Let $A_N = \ts{x \mid \abs{f(x)} \leq N \text{ for all } f \in \mathcal{F}}$.]
:::

::: {.solution}
For $N\in\mathbb Z_+$ set
\[
A_N=\{x\in X:|f(x)|\le N\text{ for every }f\in\mathcal F\}.
\]
Each $A_N$ is closed, since
\[
A_N=\bigcap_{f\in\mathcal F}f^{-1}([-N,N]).
\]
Pointwise boundedness says every $x$ belongs to some $A_N$, so $X=\bigcup_NA_N$. A complete metric space is Baire; therefore some $A_N$ has nonempty interior. Choose a nonempty open $U\subset A_N$. Then for every $x\in U$ and every $f\in\mathcal F$, $|f(x)|\le N$. Taking $M=N$ proves the assertion.
:::
