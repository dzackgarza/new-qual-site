---
schema: qual/card@1
id: E-NO7PH
kind: problem
title: Baire property of the lower limit line
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

Determine whether or not $\mathbb{R}_\ell$ is a Baire space.
:::

::: {.solution}
$\mathbb{R}_\ell$ is a Baire space. Let $G_1, G_2, \ldots$ be dense open subsets of $\mathbb{R}_\ell$ and let $U_0$ be a nonempty open subset. It suffices to show that $U_0 \cap \bigcap_n G_n \neq \varnothing$.

<1>1. There are real numbers $a_n < b_n$, $n \ge 0$, with $[a_0, b_0] \subseteq U_0$ and $[a_{n+1}, b_{n+1}] \subseteq G_{n+1} \cap [a_n, b_n)$ for $n \ge 0$.

::: {.proof}
The sets $[a, b)$ form a basis of $\mathbb{R}_\ell$. The nonempty open set $U_0$ contains some $[a_0, b_0')$; put $b_0 = (a_0 + b_0')/2$. Given $a_n < b_n$, the set $G_{n+1} \cap [a_n, b_n)$ is open, and nonempty because $G_{n+1}$ is dense. It contains some $[a_{n+1}, b')$ with $a_{n+1} < b'$; put $b_{n+1} = (a_{n+1} + b')/2$. Then $[a_{n+1}, b_{n+1}] \subseteq [a_{n+1}, b') \subseteq G_{n+1} \cap [a_n, b_n)$.
:::

<1>2. Q.E.D.

::: {.proof}
By step <1>1 the closed bounded intervals $[a_n, b_n]$ of $\RR$ are nested and nonempty, so they have a common point $x$ by compactness. Then $x \in [a_0, b_0] \subseteq U_0$ and $x \in [a_{n}, b_{n}] \subseteq G_{n}$ for every $n \ge 1$.
:::
:::
