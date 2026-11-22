---
schema: qual/card@1
id: D-AIQG3
kind: definition
title: Locally uniform convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be open and let $f_n,f\colon\Omega\to\CC$ for $n\ge1$.
The sequence $(f_n)$ \dfn{converges locally uniformly} to $f$ on $\Omega$ if $f_n\to f$ [[D-YZC3C|uniformly]] on every [[D-EILKJ|compact]] subset $K\subseteq\Omega$.

This is the convergence "uniformly on every compact subset of the region" of [@Ahl73, ch. 5, §1.1, Theorem 1], which is the hypothesis of Theorems 1 and 2 of that section.
:::

::: {.proposition}
Let $\Omega\subseteq\CC$ be open and let $f_k,f\colon\Omega\to\CC$, with the convention $\operatorname{dist}(A,\varnothing)=+\infty$ when $\Omega=\CC$.
Then $f_k\to f$ locally uniformly on $\Omega$ if and only if $f_k\to f$ uniformly on every bounded set $A\subseteq\Omega$ with $\operatorname{dist}(A,\bd\Omega)>0$.
:::
