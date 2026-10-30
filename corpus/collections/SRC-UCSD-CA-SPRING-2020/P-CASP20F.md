---
schema: qual/card@1
id: P-CASP20F
kind: problem
title: 'An entire function with bounded derivative and zeros at $\sqrt n$ is identically zero'
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Identity Theorem
  - Growth Estimates
relations: []
review: draft
---

::: {.problem}
Let $f : \CC \to \CC$ be an entire function such that $\abs{f'(z)} \leq e^{\abs{z}}$ and $f\!\left(\sqrt{n}\right) = 0$ for all positive integers $n > 0$.
Show that $f = 0$.
:::

::: {.solution}
Suppose $f\not\equiv0$. From the derivative bound, integrating along the line
segment from $0$ to $z$ gives
$$
\abs{f(z)}\le \abs{f(0)}+\abs{z}e^{\abs{z}}.
$$
Thus
$$
\log M_f(R)=O(R),
$$
where $M_f(R)=\max_{\abs{z}=R}\abs{f(z)}$.

If $f(0)=0$, factor $f(z)=z^m g(z)$ with $g(0)\ne0$; the same growth estimate
gives $\log M_g(R)=O(R+\log R)$. Hence it suffices to apply Jensen's formula
to a nonzero entire function $g$ with $g(0)\ne0$ and zeros containing all but
possibly finitely many points $\sqrt n$.

For large $R$, every $\sqrt n\le R/2$ contributes at least $\log2$ to the
Jensen sum. There are at least $\lfloor R^2/4\rfloor$ such zeros, so Jensen's
formula yields
$$
cR^2
\le \sum_{\abs{a_k}<R}\log\frac{R}{\abs{a_k}}
\le \log M_g(R)-\log\abs{g(0)}
=O(R+\log R),
$$
a contradiction. Therefore $f\equiv0$.
:::
