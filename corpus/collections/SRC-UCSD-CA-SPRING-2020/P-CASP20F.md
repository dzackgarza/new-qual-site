---
schema: qual/card@1
id: P-CASP20F
kind: problem
title: "Entire function with bounded derivative and zeros at sqrt(n) is identically zero"
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
Let $f : \mathbb{C} \to \mathbb{C}$ be an entire function such that $|f'(z)| \leq e^{|z|}$ and $f\!\left(\sqrt{n}\right) = 0$ for all positive integers $n > 0$.
Show that $f = 0$.
:::

::: {.solution}
Suppose $f\not\equiv0$. From the derivative bound, integrating along the line
segment from $0$ to $z$ gives
\[
|f(z)|\le |f(0)|+|z|e^{|z|}.
\]
Thus
\[
\log M_f(R)=O(R),
\]
where $M_f(R)=\max_{|z|=R}|f(z)|$.

If $f(0)=0$, factor $f(z)=z^m g(z)$ with $g(0)\ne0$; the same growth estimate
gives $\log M_g(R)=O(R+\log R)$. Hence it suffices to apply Jensen's formula
to a nonzero entire function $g$ with $g(0)\ne0$ and zeros containing all but
possibly finitely many points $\sqrt n$.

For large $R$, every $\sqrt n\le R/2$ contributes at least $\log2$ to the
Jensen sum. There are at least $\lfloor R^2/4\rfloor$ such zeros, so Jensen's
formula yields
\[
cR^2
\le \sum_{|a_k|<R}\log\frac{R}{|a_k|}
\le \log M_g(R)-\log|g(0)|
=O(R+\log R),
\]
a contradiction. Therefore $f\equiv0$.
:::
