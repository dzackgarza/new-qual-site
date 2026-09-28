---
schema: qual/card@1
id: FD-C7EQD
kind: definition
title: Order of a pole via limits of $(z-a)^k f(z)$
prompts:
- What does it mean for $f$ to have a pole of order $m$ at $a$?
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Singularities
relations: []
review: draft
---

::: {.definition}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc $D_r(a)\setminus\{a\}$ and let $m\ge1$ be an integer.
The function $f$ has a \dfn{pole of order $m$} at $a$ if $\lim_{z\to a}(z-a)^{m}f(z)$ exists in $\CC\setminus\{0\}$.
:::

::: {.proposition}
If $f$ has a pole of order $m$ at $a$, then

(i) $\lim_{z\to a}(z-a)^{k}f(z)=0$ for every integer $k>m$;

(ii) $\abs{(z-a)^{k}f(z)}\to\infty$ as $z\to a$ for every integer $k<m$.

In particular $m$ is the smallest integer $k$ for which $\lim_{z\to a}(z-a)^kf(z)$ exists in $\CC$, and the definition agrees with [[D-AUD6K]].
:::

::: {.proof}
Let $c\coloneqq\lim_{z\to a}(z-a)^mf(z)\neq0$.
For $k>m$, $(z-a)^kf(z)=(z-a)^{k-m}\cdot(z-a)^mf(z)\to0\cdot c=0$.
For $k<m$, $\abs{(z-a)^kf(z)}=\abs{z-a}^{k-m}\abs{(z-a)^mf(z)}$, where the first factor tends to $\infty$ and the second to $\abs{c}>0$.
Finally, $h(z)\coloneqq(z-a)^mf(z)$ is bounded near $a$, so by [[D-BQLJV|Riemann's removable singularity theorem]] it extends holomorphically with $h(a)=c\neq0$, and $f(z)=(z-a)^{-m}h(z)$ is a pole of order $m$ in the sense of [[D-AUD6K]]; conversely such a factorization gives $(z-a)^mf(z)=h(z)\to h(a)\neq0$.
:::
