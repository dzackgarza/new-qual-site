---
schema: qual/card@1
id: P-MICNK
kind: problem
title: $az^n+z+1$ has a root in $|z|\le 2$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
---

:::{.problem}
Let $a\in \CC$ and $n\geq 2$.
Show that the following polynomial has one root in $\abs{z} \leq 2$:
\[
f(z) = az^n + z + 1
.\]
:::

:::{.solution}
The key step: getting the following inequality to work
\[
\abs{az^n} = \abs{a}\abs{z}^n < c \leq 1 = \abs{ \abs{z} - \abs{1} } \leq \abs{z+1} 
.\]
If this is true, then $1 = \size Z_{z+1} = \size Z_f$.
If $\abs{a} < 2^n$, this holds because $\abs{a}\abs{z}^n < {1\over 2^n} 2^n = 1$, so taking $c\da 1$ works.

Otherwise, suppose $\abs{a} \geq 2^n$.
Letting $z_k$ be the roots of $f$ and considering the constant coefficient, we have
\[
a\prod_{k\leq n} z_k = 1 \implies \abs{ \prod_{k\leq n} z_k } = \abs{1\over a} \leq 2^n
,\]
so not every $z_k$ can satisfy $\abs{z_k} > 2$ and at least one is in $\abs{z} \leq 2$.
:::

