---
schema: qual/card@1
id: E-3SU0X
kind: problem
title: Quotient topology on a three-point image of the line
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Check the details of Example 3 of §22: for the map $p: \mathbb{R} \to A = \ts{a, b, c}$ defined by

$$
p(x) =
\begin{cases}
a & \text{if } x > 0, \\
b & \text{if } x < 0, \\
c & \text{if } x = 0,
\end{cases}
$$

determine the quotient topology on $A$ induced by $p$.
:::

::: {.solution}
<1>1. The preimages of the subsets of $A$ are $p^{-1}(\varnothing)=\varnothing$, $p^{-1}(\{a\})=(0,\infty)$, $p^{-1}(\{b\})=(-\infty,0)$, $p^{-1}(\{a,b\})=\mathbb R-\{0\}$, $p^{-1}(A)=\mathbb R$, which are open, and $p^{-1}(\{c\})=\{0\}$, $p^{-1}(\{a,c\})=[0,\infty)$, $p^{-1}(\{b,c\})=(-\infty,0]$, which are not open.

::: {.proof}
The preimages follow from the definition of $p$.
The last three each contain $0$ but no open interval about $0$.
:::

<1>2. Q.E.D.

::: {.proof}
A subset $U\subseteq A$ is open in the quotient topology if and only if $p^{-1}(U)$ is open, so by step <1>1 the quotient topology is
$$
\boxed{\bigl\{\varnothing,\{a\},\{b\},\{a,b\},A\bigr\}}.
$$
:::
:::
