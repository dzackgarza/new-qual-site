---
schema: qual/card@1
id: PR-H4CYN
kind: proposition
title: A Taylor series converges to $f$ when $\abs{f^{(n)}}\leq M^n$
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Series of Functions
relations: []
review: draft
---

::: {.proposition}
Let $c\in\RR$, $\varepsilon>0$, and $f\in C^\infty((c-\varepsilon,c+\varepsilon))$ with values in $\RR$.
Suppose there exists $M\geq0$ such that
$$
\abs{f^{(n)}(x)} \leq M^n \quad\text{for all } n\geq0 \text{ and all } x\in(c-\varepsilon,c+\varepsilon).
$$
Then for every $x\in(c-\varepsilon,c+\varepsilon)$,
$$
f(x)=\sum_{n=0}^\infty\frac{f^{(n)}(c)}{n!}(x-c)^n .
$$
:::

::: {.proof}
Fix $x\in(c-\varepsilon,c+\varepsilon)$ and $N\geq0$.
By Taylor's theorem with the Lagrange remainder, there is $\xi$ between $c$ and $x$ with
$$
\abs{f(x)-\sum_{n=0}^N\frac{f^{(n)}(c)}{n!}(x-c)^n}=\frac{\abs{f^{(N+1)}(\xi)}}{(N+1)!}\abs{x-c}^{N+1}\leq\frac{(M\varepsilon)^{N+1}}{(N+1)!},
$$
and $a^{N+1}/(N+1)!\to0$ as $N\to\infty$ for every $a\geq0$.
:::
