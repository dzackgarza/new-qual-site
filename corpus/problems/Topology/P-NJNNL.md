---
schema: qual/card@1
id: P-NJNNL
kind: problem
title: Continuous images of compact spaces, and compact metric spaces are complete
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuity
  - Completeness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
(1) Let $X$ and $Y$ be topological spaces, and let $f: X \to Y$ be a continuous map.
Prove that if $X$ is **compact**, then its image $f(X) \subseteq Y$ is compact.
(2) Let $(X, d)$ be a metric space.
Prove that if $X$ is **compact**, then $(X, d)$ is **complete** (every Cauchy sequence in $X$ converges to a limit in $X$).
:::

::: solution
<1>1. If $X$ is compact and $f:X\to Y$ is continuous, then $f(X)$ is compact.
::: proof
Let $\{V_\alpha\}$ be an open cover of $f(X)$. Then $\{f^{-1}(V_\alpha)\}$ is an open cover of $X$. Compactness gives finitely many indices $\alpha_1,\dots,\alpha_r$ with
$$
X=\bigcup_{j=1}^r f^{-1}(V_{\alpha_j}).
$$
Applying $f$ shows
$$
f(X)\subseteq\bigcup_{j=1}^r V_{\alpha_j},
$$
so the original cover has a finite subcover.
:::

<1>2. Every compact metric space is complete.
::: proof
Let $(x_n)$ be Cauchy in compact metric $X$. Compact metric spaces are sequentially compact, so some subsequence $x_{n_k}$ converges to a point $x\in X$.

Given $\varepsilon>0$, choose $N$ so that
$$
d(x_m,x_n)<\varepsilon/2\qquad(m,n\ge N).
$$
Choose $k$ with $n_k\ge N$ and $d(x_{n_k},x)<\varepsilon/2$. Then for every $n\ge N$,
$$
d(x_n,x)\le d(x_n,x_{n_k})+d(x_{n_k},x)<\varepsilon.
$$
Thus $x_n\to x$, so every Cauchy sequence converges in $X$.
:::
:::
