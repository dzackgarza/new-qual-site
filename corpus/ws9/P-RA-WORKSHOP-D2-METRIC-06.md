---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-06
kind: problem
title: 'The sum metric on a product and compact products'
classification:
  areas:
  - real-analysis
  topics:
  - metric-spaces
  - compactness
relations: []
review: draft
---

:::{.problem title="?"}
(May 2019, #1) Let $(M,d_M)$ and $(N,d_N)$ be metric spaces. Define
$d_{M\times N}:(M\times N)\times(M\times N)\to\mathbb R$ by
$$
d_{M\times N}((x_1,y_1),(x_2,y_2)):=d_M(x_1,x_2)+d_N(y_1,y_2).
$$

1) Prove that $(M\times N,d_{M\times N})$ is a metric space.

2) Let $S\subseteq M$ and $T\subseteq N$ be compact sets in $(M,d_M)$ and $(N,d_N)$, respectively. Prove
that $S\times T$ is a compact set in $(M\times N,d_{M\times n})$.
:::

::: remark
The final displayed product-metric subscript is printed as $M\times n$ in the source; the definition immediately above uses $M\times N$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. (1) $d_{M\times N}$ is a metric.
<2>1. Non-negativity and symmetry: $d_M \ge 0$, $d_N \ge 0$, and both are symmetric, so $d_{M\times N}((x_1,y_1),(x_2,y_2)) = d_M(x_1,x_2)+d_N(y_1,y_2) = d_{M\times N}((x_2,y_2),(x_1,y_1))$.
<2>2. Separation: $d_{M\times N}((x_1,y_1),(x_2,y_2)) = 0$ iff $d_M(x_1,x_2) = 0$ and $d_N(y_1,y_2) = 0$ (both terms are non-negative) iff $x_1 = x_2$ and $y_1 = y_2$.
<2>3. Triangle inequality: for a third point $(x_3,y_3)$,
    \[d_{M\times N}((x_1,y_1),(x_2,y_2)) = d_M(x_1,x_2)+d_N(y_1,y_2) \le \big(d_M(x_1,x_3)+d_M(x_3,x_2)\big) + \big(d_N(y_1,y_3)+d_N(y_3,y_2)\big) = d_{M\times N}((x_1,y_1),(x_3,y_3)) + d_{M\times N}((x_3,y_3),(x_2,y_2)),\]
    using the triangle inequality for $d_M$ and $d_N$ separately.
<1>2. (2) $S \times T$ is compact in $M\times N$.
    Proof: $M\times N$ is a metric space, so compactness is equivalent to sequential compactness. Let $\{(x_k, y_k)\}$ be a sequence in $S\times T$. Since $S$ is compact, a subsequence $\{x_{k_j}\}$ converges in $S$; since $T$ is compact, a further subsequence $\{y_{k_{j_\ell}}\}$ converges in $T$. Then $d_{M\times N}((x_{k_{j_\ell}}, y_{k_{j_\ell}}), (x, y)) = d_M(x_{k_{j_\ell}}, x) + d_N(y_{k_{j_\ell}}, y) \to 0$, so a subsequence converges in $S\times T$. Hence $S\times T$ is compact.
<1>3. Q.E.D.
:::
