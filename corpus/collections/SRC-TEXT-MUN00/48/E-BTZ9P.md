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
---

::: {.exercise}

If $f_n$ is a sequence of continuous functions $f_n: \mathbb{R} \to \mathbb{R}$ such that $f_n(x) \to f(x)$ for each $x \in \mathbb{R}$, show that $f$ is continuous at uncountably many points of $\mathbb{R}$.
:::

::: {.solution}
For $\varepsilon > 0$ and $N \ge 1$ put
$$A_N(\varepsilon) = \{x \in \RR : \abs{f_m(x) - f_k(x)} \le \varepsilon \text{ for all } m, k \ge N\}, \qquad U(\varepsilon) = \bigcup_{N \ge 1} \operatorname{Int} A_N(\varepsilon).$$
The space $\RR$ is a complete metric space, hence a Baire space by the Baire category theorem.

<1>1. Each $A_N(\varepsilon)$ is closed, and $\bigcup_N A_N(\varepsilon) = \RR$.

::: {.proof}
$A_N(\varepsilon)$ is an intersection of the closed sets $\{x : \abs{f_m(x) - f_k(x)} \le \varepsilon\}$, which are closed because $f_m - f_k$ is continuous. For each $x$, the sequence $(f_n(x))$ converges, hence is Cauchy, so $x \in A_N(\varepsilon)$ for some $N$.
:::

<1>2. $U(\varepsilon)$ is open and dense in $\RR$.

::: {.proof}
$U(\varepsilon)$ is a union of open sets. Let $V$ be a nonempty open interval. The closed subsets $A_N(\varepsilon) \cap \overline{V}$ of the complete metric space $\overline{V}$ cover $\overline{V}$ by step <1>1, so by the Baire category theorem one of them has nonempty interior in $\overline{V}$; that interior meets $V$, so it contains a nonempty open interval $J \subseteq V \cap A_N(\varepsilon)$. Then $J \subseteq \operatorname{Int} A_N(\varepsilon)$, so $V$ meets $U(\varepsilon)$.
:::

<1>3. $f$ is continuous at every point of $C = \bigcap_{k \ge 1} U(1/k)$.

::: {.proof}
Let $x \in C$ and $\varepsilon > 0$; choose $k$ with $1/k < \varepsilon/3$. Then $x \in W = \operatorname{Int} A_N(1/k)$ for some $N$. For $y \in W$ and $m \ge N$, $\abs{f_m(y) - f_N(y)} \le 1/k$; letting $m \to \infty$ gives $\abs{f(y) - f_N(y)} \le 1/k$. By continuity of $f_N$, there is a neighborhood $V \subseteq W$ of $x$ with $\abs{f_N(y) - f_N(x)} < 1/k$ for $y \in V$. For $y \in V$,
$$\abs{f(y) - f(x)} \le \abs{f(y) - f_N(y)} + \abs{f_N(y) - f_N(x)} + \abs{f_N(x) - f(x)} < 3/k < \varepsilon.$$
:::

<1>4. $C$ is uncountable.

::: {.proof}
Suppose $C = \{c_1, c_2, \ldots\}$ is countable. The sets $U(1/k)$ and $\RR \setminus \{c_j\}$ form a countable family of dense open subsets of $\RR$ by step <1>2, and their intersection is $C \setminus C = \varnothing$. This contradicts the Baire property of $\RR$. A finite $C$ is excluded in the same way.
:::

<1>5. Q.E.D.

::: {.proof}
By steps <1>3 and <1>4, $f$ is continuous at every point of the uncountable set $C$.
:::
:::
