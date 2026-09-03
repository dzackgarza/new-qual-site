---
schema: qual/card@1
id: E-9LY2B
kind: problem
title: Infinite wedges of circles are not first countable
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that if $X$ is an infinite wedge of circles, then $X$ does not satisfy the first countability axiom.
:::

::: solution
**Goal:** Prove that an infinite wedge sum of circles $X = \bigvee_{\alpha \in J} S_\alpha^1$ fails to be first-countable at the common wedge basepoint $p$.

<1>1. Quotient topology on the wedge sum:
    *Proof:*
    <2>1. By definition of the wedge sum $X = (\coprod_{\alpha \in J} S_\alpha^1) / \{p_\alpha\}$, a subset $U \subseteq X$ containing the basepoint $p$ is open in $X$ if and only if for every $\alpha \in J$, the intersection $U \cap S_\alpha^1$ is open in $S_\alpha^1$.

<1>2. Setting up proof by contradiction:
    *Proof:*
    <2>1. Suppose for contradiction that $p$ has a countable local neighborhood basis $\{U_n\}_{n=1}^\infty$ of open sets in $X$.
    <2>2. Since $J$ is infinite, choose a countably infinite subset of distinct indices $\{\alpha_n\}_{n=1}^\infty \subseteq J$.

<1>3. Diagonal construction of an open neighborhood $V$:
    *Proof:*
    <2>1. For each $n \ge 1$, $U_n \cap S_{\alpha_n}^1$ is an open neighborhood of $p$ in $S_{\alpha_n}^1$.
    <2>2. Since $S_{\alpha_n}^1 \cong S^1$ has no isolated points, choose a point $x_n \in (U_n \cap S_{\alpha_n}^1) \setminus \{p\}$.
    <2>3. Define $V \subseteq X$ by setting its intersection with each circle:
        $$V \cap S_{\alpha_n}^1 = S_{\alpha_n}^1 \setminus \{x_n\} \quad \text{for all } n \ge 1,$$
        $$V \cap S_\beta^1 = S_\beta^1 \quad \text{for all } \beta \in J \setminus \{\alpha_n \mid n \ge 1\}.$$
    <2>4. For every $\alpha \in J$, $V \cap S_\alpha^1$ is open in $S_\alpha^1$ and contains $p$ (since $x_n \neq p$).
    <2>5. By the definition of the quotient topology in <1>1, $V$ is an open neighborhood of $p$ in $X$.

<1>4. Deriving the contradiction:
    *Proof:*
    <2>1. If $\{U_n\}_{n=1}^\infty$ were a local neighborhood basis at $p$, there would exist an index $k \ge 1$ such that $U_k \subseteq V$.
    <2>2. By construction, $x_k \in U_k$.
    <2>3. However, $x_k \notin S_{\alpha_k}^1 \setminus \{x_k\} = V \cap S_{\alpha_k}^1$, so $x_k \notin V$.
    <2>4. This contradicts $U_k \subseteq V$.

<1>5. Conclusion:
    $X$ has no countable local basis at $p$, and therefore $X$ is not first-countable. Q.E.D.
:::
