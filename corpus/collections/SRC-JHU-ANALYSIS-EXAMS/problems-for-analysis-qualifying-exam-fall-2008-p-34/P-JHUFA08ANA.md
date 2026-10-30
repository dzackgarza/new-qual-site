---
schema: qual/card@1
id: P-JHUFA08ANA
kind: problem
title: 'Iteration of $s\mapsto s^2$ on $[0,1]$: pushforward measures and their weak limit'
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Weak Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Consider the mapping $F \colon [0, 1] \to [0, 1]$ given by $F(s) = s^{2}$.

Let $F^{-j}(A)$ be the inverse image of $j$ iterates of $F$ applied to a measurable subset $A \subset [0, 1]$. That is, if $F = F^{1}$ and $F^{j}$, $j = 2, 3, \ldots$, is defined inductively as $F^{j} = F^{j-1} \circ F$, then $F^{-j}(A) = \{x \st F^{j}x = y \text{ for some } y \in A\}$.

(a) Given $N = 1, 2, \dots$, show that $\mu_{N}(A) = N^{-1}\sum_{j < N} \setmeasure{F^{-j}(A)}$ is a measure which is absolutely continuous with respect to Lebesgue measure. Here $\setmeasure{B}$ denotes the Lebesgue measure of a measurable set.

(b) Show that $\mu_{N}([a, b]) \to 0$ if $0 < a < b \leq 1$.

(c) If $f$ is a continuous function on $[0, 1]$ does
$$
\lim_{N \to \infty} \int_{[0, 1]} f(s) \, d\mu_{N}(s)
$$
tend to a limit? If so, what is the limit?
:::

::: {.solution}
For each $j \ge 0$, let
$$
\nu_j(A):=\setmeasure{F^{-j}(A)} = \setmeasure{\{s\in[0,1]:F^j(s)\in A\}}.
$$

*a)*  For any measurable sets $(A_n)$ that are pairwise disjoint,
$(\nu_j(\bigsqcup A_n))=\setmeasure{F^{-j}(\bigsqcup A_n)}=\sum \setmeasure{F^{-j}(A_n)}=\sum\nu_j(A_n)$.
So $\nu_j$ is a measure on Borel sets.
Here $F^j(s)=s^{2^j}$ and so $F^{-j}(A)=\{t^{2^{-j}}:t\in A\}$, the image of $A$ under the map $g_j(t)=t^{2^{-j}}$.
Since
$$g_j'(t)=2^{-j}t^{2^{-j}-1}\in L^1[0,1],$$
$g_j$ is absolutely continuous and has Luzin’s property (N), hence $\setmeasure{A}=0\Rightarrow \setmeasure{\{t^{2^{-j}}:t\in A\}}=0$.
Therefore $\nu_j\ll \setmeasure{\cdot}$.

Now $\mu_N=\frac1N\sum_{j=0}^{N-1}\nu_j$, so $\mu_N$ is a measure and
$\mu_N\ll$ Lebesgue.

*b)*  Since $F^j$ is increasing,
$$
F^{-j}([a,b])=[a^{2^{-j}},b^{2^{-j}}],
$$
hence
$$
\mu_N([a,b])=\frac1N\sum_{j=0}^{N-1}\bigl(b^{2^{-j}}-a^{2^{-j}}\bigr).
$$
Each term tends to $0$ as $j\to\infty$ (because $0<a<b\le1$), and the sequence is bounded.
Its Cesàro mean therefore tends to $0$.

*c)*  For bounded measurable $f$,
$$
\int_0^1 f\,d\mu_N
=\frac1N\sum_{j=0}^{N-1}\int_0^1 f\,d\nu_j
=\frac1N\sum_{j=0}^{N-1}\int_0^1 f(F^j(s))\,ds
$$
with
$$
\int_0^1 f\,d\nu_j=\int_0^1 f(s^{2^j})\,ds.
$$
For each $s\in[0,1)$, $s^{2^j}\to0$, so $f(s^{2^j})\to f(0)$ and dominated convergence gives
$$
\lim_{j\to\infty}\int_0^1 f(s^{2^j})\,ds=f(0).
$$
Therefore the Cesàro average of the first $N$ terms converges to $f(0)$:
$$
\lim_{N\to\infty}\int_0^1 f\,d\mu_N=f(0).
$$
So the limit exists and equals $f(0)$.
:::
