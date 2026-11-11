---
schema: qual/card@1
id: E-BTZ9P
kind: problem
title: Pointwise limits of continuous functions on $\RR$ are continuous at uncountably many points
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §48 Exercise 8 (printed p. 299) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book: the sets
    A_N(eps) are closed and their union is R because a convergent sequence is Cauchy; U(eps) is dense because in
    the complete space closure of an interval the closed sets A_N cap closure V cover, so one has interior in
    that closure by Theorem 48.2, and a nonempty open subset of a closure meets the interval itself; at a point
    of the intersection of the U(1/k) the three-term estimate with f_N is the argument of Theorem 48.5; and the
    set C is uncountable because otherwise the dense open sets U(1/k) together with the complements of the
    points of C would have empty intersection, contradicting Theorem 48.2. Nothing needed correction.
---

::: {.exercise}

If $f_n$ is a sequence of continuous functions $f_n: \RR \to \RR$ such that $f_n(x) \to f(x)$ for each $x \in \RR$, show that $f$ is continuous at uncountably many points of $\RR$.
:::

::: {.solution}
For $\varepsilon > 0$ and $N \ge 1$ put
$$A_N(\varepsilon) = \{x \in \RR : \abs{f_m(x) - f_k(x)} \le \varepsilon \text{ for all } m, k \ge N\}, \qquad U(\varepsilon) = \bigcup_{N \ge 1} \operatorname{Int} A_N(\varepsilon).$$
The space $\RR$ is a complete metric space, hence a Baire space by the Baire category theorem.

::: pf

::: {.pf-step #s1}

Each $A_N(\varepsilon)$ is closed, and $\bigcup_N A_N(\varepsilon) = \RR$.

::: pf-proof

$A_N(\varepsilon)$ is an intersection of the closed sets $\{x : \abs{f_m(x) - f_k(x)} \le \varepsilon\}$, which are closed because $f_m - f_k$ is continuous. For each $x$, the sequence $(f_n(x))$ converges, hence is Cauchy, so $x \in A_N(\varepsilon)$ for some $N$.

:::

:::

::: {.pf-step #s2}

$U(\varepsilon)$ is open and dense in $\RR$.

::: pf-proof

$U(\varepsilon)$ is a union of open sets. Let $V$ be a nonempty open interval. The closed subsets $A_N(\varepsilon) \cap \overline{V}$ of the complete metric space $\overline{V}$ cover $\overline{V}$ by step [](#s1){.pf-ref}, so by the Baire category theorem one of them has nonempty interior in $\overline{V}$; that interior meets $V$, so it contains a nonempty open interval $J \subseteq V \cap A_N(\varepsilon)$. Then $J \subseteq \operatorname{Int} A_N(\varepsilon)$, so $V$ meets $U(\varepsilon)$.

:::

:::

::: {.pf-step #s3}

$f$ is continuous at every point of $C = \bigcap_{k \ge 1} U(1/k)$.

::: pf-proof

Let $x \in C$ and $\varepsilon > 0$; choose $k$ with $1/k < \varepsilon/3$. Then $x \in W = \operatorname{Int} A_N(1/k)$ for some $N$. For $y \in W$ and $m \ge N$, $\abs{f_m(y) - f_N(y)} \le 1/k$; letting $m \to \infty$ gives $\abs{f(y) - f_N(y)} \le 1/k$. By continuity of $f_N$, there is a neighborhood $V \subseteq W$ of $x$ with $\abs{f_N(y) - f_N(x)} < 1/k$ for $y \in V$. For $y \in V$,
$$\abs{f(y) - f(x)} \le \abs{f(y) - f_N(y)} + \abs{f_N(y) - f_N(x)} + \abs{f_N(x) - f(x)} < 3/k < \varepsilon.$$

:::

:::

::: {.pf-step #s4}

$C$ is uncountable.

::: pf-proof

Suppose $C = \{c_1, c_2, \ldots\}$ is countable. The sets $U(1/k)$ and $\RR \setminus \{c_j\}$ form a countable family of dense open subsets of $\RR$ by step [](#s2){.pf-ref}, and their intersection is $C \setminus C = \varnothing$. This contradicts the Baire property of $\RR$. A finite $C$ is excluded in the same way.

:::

:::

::: pf-qed

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, $f$ is continuous at every point of the uncountable set $C$.

:::

:::

:::
