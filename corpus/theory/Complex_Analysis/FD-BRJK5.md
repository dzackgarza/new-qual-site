---
schema: qual/card@1
id: FD-BRJK5
kind: definition
title: Removable singularity and boundedness near it
prompts:
- What is a removable singularity, and how does $f$ behave near one?
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Singularities
relations: []
review: draft
---

::: {.definition}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc $D_r(z_0)\setminus\{z_0\}$.
The point $z_0$ is a \dfn{removable singularity} of $f$ if there exist $0<\rho\le r$ and a holomorphic function $g\colon D_\rho(z_0)\to\CC$ with $f=g$ on $D_\rho(z_0)\setminus\{z_0\}$.
:::

::: {.proposition}
Let $f$ be holomorphic on $D_r(z_0)\setminus\{z_0\}$.
The following are equivalent.

(a) $z_0$ is a removable singularity of $f$.

(b) $\lim_{z\to z_0}f(z)$ exists in $\CC$.

(c) $f$ is bounded on $D_\rho(z_0)\setminus\{z_0\}$ for some $0<\rho\le r$.

(d) There are an integer $n\le0$ and a function $h$ holomorphic on a neighborhood of $z_0$ with $f(z)=(z-z_0)^{-n}h(z)$ for $z\neq z_0$ near $z_0$.
:::

::: {.proof}
(a)$\Rightarrow$(b): $f(z)=g(z)\to g(z_0)$.
(b)$\Rightarrow$(c): a function with a finite limit at $z_0$ is bounded near $z_0$.
(c)$\Rightarrow$(a) is [[D-BQLJV|Riemann's removable singularity theorem]].
(a)$\Rightarrow$(d): take $n=0$ and $h=g$.
(d)$\Rightarrow$(a): $g(z)\coloneqq(z-z_0)^{-n}h(z)$ is holomorphic near $z_0$ because $-n\ge0$.
:::

::: {.remark}
Condition (d) is the factorization $f=(z-z_0)^{-n}h$ that defines a [[D-AUD6K|pole of order $n$]] for $n\ge1$, allowed here with $n\le0$; in this sense a removable singularity is sometimes called a pole of order zero.
:::
