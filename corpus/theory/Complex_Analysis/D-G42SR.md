---
schema: qual/card@1
id: D-G42SR
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
Let $\Omega\subseteq\CC$ be open and let $f_k,f\colon\Omega\to\CC$ for $k\ge1$.
The sequence $(f_k)$ \dfn{converges locally uniformly} to $f$ on $\Omega$ if $f_k\to f$ [[D-YZC3C|uniformly]] on every [[D-EILKJ|compact]] subset of $\Omega$.
:::

::: {.proposition}
Let $\Omega\subseteq\CC$ be open and let $f_k,f\colon\Omega\to\CC$, with the convention $\operatorname{dist}(A,\varnothing)=+\infty$ when $\Omega=\CC$.
Then $f_k\to f$ locally uniformly on $\Omega$ if and only if $f_k\to f$ uniformly on every bounded set $A\subseteq\Omega$ with $\operatorname{dist}(A,\partial\Omega)>0$.
:::

::: {.proof}
Let $A\subseteq\Omega$ be bounded with $\operatorname{dist}(A,\partial\Omega)=d>0$.
Its closure $\overline A$ is closed and bounded, hence compact, and every point of $\overline A$ has distance at least $d$ from $\partial\Omega$.
A point of $\overline A$ lies in $\overline\Omega$ but not in $\partial\Omega$, so it lies in $\Omega$; thus $\overline A$ is a compact subset of $\Omega$, and uniform convergence on $\overline A$ gives uniform convergence on $A$.

Conversely, let $K\subseteq\Omega$ be compact.
Then $K$ is bounded, and $z\mapsto\operatorname{dist}(z,\partial\Omega)$ is continuous and positive on $K$ when $\partial\Omega\neq\varnothing$, because $\partial\Omega$ is closed and disjoint from $K$, so it has a positive minimum on $K$.
Hence $K$ is one of the sets $A$.
:::
