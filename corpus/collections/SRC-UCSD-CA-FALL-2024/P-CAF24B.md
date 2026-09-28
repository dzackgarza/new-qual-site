---
schema: qual/card@1
id: P-CAF24B
kind: problem
title: Entire function with a rational Taylor coefficient at every real point is a polynomial
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Entire Functions
relations: []
review: draft
---

::: {.problem}
Let $f : \mathbb{C} \to \mathbb{C}$ be an entire function.
Assume that for any $a \in \mathbb{R}$, at least one coefficient in the Taylor expansion of $f$ around $a$ is a rational number.
Prove that $f$ is a polynomial.
:::

::: {.solution}
For $n\ge0$ and $q\in\mathbb Q$, define
\[
E_{n,q}
=\left\{a\in\mathbb R:
\frac{f^{(n)}(a)}{n!}=q\right\}.
\]
Each $E_{n,q}$ is closed in $\mathbb R$, and by hypothesis
\[
\mathbb R=\bigcup_{n\ge0}\bigcup_{q\in\mathbb Q}E_{n,q}.
\]
This is a countable union of closed sets. By the Baire category theorem, some
$E_{n,q}$ has nonempty interior. Hence for some open interval $I\subset\mathbb R$,
\[
f^{(n)}(a)=n!q
\qquad(a\in I).
\]
The entire function $f^{(n)}-n!q$ vanishes on an interval, so the identity
theorem gives
\[
f^{(n)}\equiv n!q
\]
on $\mathbb C$. Therefore $f^{(n+1)}\equiv0$, and $f$ is a polynomial of
degree at most $n$.
:::
