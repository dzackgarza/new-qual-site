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
Let $f : \CC \to \CC$ be an entire function.
Assume that for any $a \in \RR$, at least one coefficient in the Taylor expansion of $f$ around $a$ is a rational number.
Prove that $f$ is a polynomial.
:::

::: {.solution}
For $n\ge0$ and $q\in\QQ$, define
$$
E_{n,q}
=\left\{a\in\RR:
\frac{f^{(n)}(a)}{n!}=q\right\}.
$$
Each $E_{n,q}$ is closed in $\RR$, and by hypothesis
$$
\RR=\bigcup_{n\ge0}\bigcup_{q\in\QQ}E_{n,q}.
$$
This is a countable union of closed sets. By the Baire category theorem, some
$E_{n,q}$ has nonempty interior. Hence for some open interval $I\subset\RR$,
$$
f^{(n)}(a)=n!q
\qquad(a\in I).
$$
The entire function $f^{(n)}-n!q$ vanishes on an interval, so the identity
theorem gives
$$
f^{(n)}\equiv n!q
$$
on $\CC$. Therefore $f^{(n+1)}\equiv0$, and $f$ is a polynomial of
degree at most $n$.
:::
