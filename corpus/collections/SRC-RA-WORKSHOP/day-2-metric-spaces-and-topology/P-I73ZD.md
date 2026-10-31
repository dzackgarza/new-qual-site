---
schema: qual/card@1
id: P-I73ZD
kind: problem
title: The sum metric $d_M+d_N$ on $M\times N$, and compactness of a product of compact
  sets
classification:
  areas:
  - real-analysis
  topics:
  - Metric Spaces
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $(M, d_M)$, $(N, d_N)$ be metric spaces. Define
$d_{M \times N} \colon (M \times N) \times (M \times N) \to \RR$
by
$$d_{M \times N}((x_1, y_1), (x_2, y_2)) \coloneqq d_M(x_1, x_2) + d_N(y_1, y_2).$$

(a) Prove that $(M \times N, d_{M \times N})$ is a metric space.

(b) Let $S \subseteq M$ and $T \subseteq N$ be compact sets in
$(M, d_M)$ and $(N, d_N)$, respectively. Prove that $S \times T$
is a compact set in $(M \times N, d_{M \times N})$.
:::

::: {.solution}

::: pf

::: pf-step

$(M\times N, d_{M\times N})$ is a metric space.

::: pf-proof

::: pf-step

$d_{M\times N} \ge 0$, and $d_{M\times N}((x_1,y_1),(x_2,y_2)) = 0$ if and only if $(x_1,y_1) = (x_2,y_2)$.

::: pf-proof

$d_{M\times N}((x_1,y_1),(x_2,y_2)) = d_M(x_1,x_2) + d_N(y_1,y_2)$ is a sum of two nonnegative numbers, so it vanishes if and only if $d_M(x_1,x_2) = 0$ and $d_N(y_1,y_2) = 0$, that is, $x_1 = x_2$ and $y_1 = y_2$.

:::

:::

::: pf-step

$d_{M\times N}(p, q) = d_{M\times N}(q, p)$ for all $p, q \in M \times N$.

::: pf-proof

$d_M$ and $d_N$ are symmetric, so their sum is.

:::

:::

::: pf-step

$d_{M\times N}(p_1, p_3) \le d_{M\times N}(p_1, p_2) + d_{M\times N}(p_2, p_3)$ for $p_i = (x_i, y_i)$.

::: pf-proof

By the triangle inequalities in $M$ and $N$,
$$d_{M\times N}(p_1,p_3) = d_M(x_1,x_3) + d_N(y_1,y_3) \le d_M(x_1,x_2) + d_M(x_2,x_3) + d_N(y_1,y_2) + d_N(y_2,y_3),$$
and the right side regroups as $d_{M\times N}(p_1, p_2) + d_{M\times N}(p_2, p_3)$.

:::

:::

:::

:::

::: pf-step

$S \times T$ is compact in $(M\times N, d_{M\times N})$.

::: pf-proof

In a metric space compactness is equivalent to sequential compactness, so it suffices to show that every sequence $((s_k, t_k))$ in $S \times T$ has a subsequence converging in $S\times T$.

::: pf-step

Some subsequence satisfies $s_{k_j} \to s \in S$ and $t_{k_j} \to t \in T$.

::: pf-proof

$S$ is sequentially compact, so $(s_k)$ has a subsequence converging to some $s \in S$.
$T$ is sequentially compact, so the corresponding subsequence of $(t_k)$ has a further subsequence converging to some $t \in T$; along it the first coordinates still converge to $s$.

:::

:::

::: pf-step

Along that subsequence, $(s_{k_j}, t_{k_j}) \to (s, t)$ in $d_{M\times N}$.

::: pf-proof

$d_{M\times N}((s_{k_j},t_{k_j}),(s,t)) = d_M(s_{k_j}, s) + d_N(t_{k_j}, t) \to 0$.

:::

:::

:::

:::

:::

:::
