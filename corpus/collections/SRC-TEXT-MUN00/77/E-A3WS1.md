---
schema: qual/card@1
id: E-A3WS1
kind: problem
title: Reducing schemes of ten sides to standard form
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $w$ be a proper labelling scheme for a 10-sided polygonal region.
If $w$ is of projective type, which of the list of spaces in Theorem 77.5 can it represent?
What if $w$ is of torus type?
:::

::: {.solution}
**Goal:** Determine all topological surfaces from Theorem 77.5 represented by a proper labeling scheme $w$ on a 10-sided polygon, in both the projective and torus cases.

::: pf

::: pf-step
General classification principles (§77):

::: pf-proof

::: pf-step
A proper labeling scheme $w$ on a 10-sided polygon has $m = 5$ pairs of matched edges.
:::

::: pf-step
By the classification reduction algorithm (Theorem 77.5):
- A scheme of **projective type** reduces to a standard non-orientable normal form $c_1 c_1 c_2 c_2 \cdots c_k c_k$, representing the connected sum of $k$ real projective planes ($k \mathbb{P}^2$ or $P_k$). Each cross-cap block $c_i c_i$ uses $2$ edges.
- A scheme of **torus type** reduces either to the empty word / 2-sphere ($S^2$) or to a standard orientable normal form $(a_1 b_1 a_1^{-1} b_1^{-1}) \cdots (a_g b_g a_g^{-1} b_g^{-1})$, representing the connected sum of $g$ tori ($g T^2$ or $T_g$). Each handle block uses $4$ edges.
:::

::: pf-step
In the reduction steps, collapsing elementary adjacent inverse pairs ($x x^{-1}$) reduces the edge count by $2$. Thus the standard form has $2k \le 10$ edges (for projective type) and $4g \le 10$ edges (for torus type).
:::

:::

:::

::: pf-step
Case 1: $w$ is of projective type.

::: pf-proof

::: pf-step
Since $w$ is of projective type, at least one pair of edges occurs with the same orientation, so the genus is non-orientable ($k \ge 1$).
:::

::: pf-step
The number of projective planes $k$ satisfies $2k \le 10$, which implies $1 \le k \le 5$.
:::

::: pf-step
Each value $k \in \{1, 2, 3, 4, 5\}$ can be realized by adding $5 - k$ pairs of adjacent cancelling edges $x x^{-1}$ to the standard $2k$-sided form.
:::

::: pf-step
Thus, $w$ can represent:
- $k = 1$: $\mathbb{P}^2$ (the real projective plane),
- $k = 2$: $2\mathbb{P}^2 = \mathbb{P}^2 \# \mathbb{P}^2$ (the Klein bottle),
- $k = 3$: $3\mathbb{P}^2$,
- $k = 4$: $4\mathbb{P}^2$,
- $k = 5$: $5\mathbb{P}^2$.
:::

:::

:::

::: pf-step
Case 2: $w$ is of torus type.

::: pf-proof

::: pf-step
Since $w$ is of torus type, every letter appears once with exponent $+1$ and once with exponent $-1$, so the resulting surface is orientable.
:::

::: pf-step
The number of handles $g$ satisfies $4g \le 10$, which implies $g \in \{0, 1, 2\}$.
:::

::: pf-step
Each value $g \in \{0, 1, 2\}$ is realized:
- $g = 0$: $S^2$ (the 2-sphere, when all 5 pairs cancel as trivial bubbles),
- $g = 1$: $T^2$ (the torus, using 4 edges plus 3 cancelled pairs),
- $g = 2$: $T^2 \# T^2$ (the double torus, using 8 edges plus 1 cancelled pair).
:::

::: pf-step
Thus, $w$ can represent:
- $S^2$ (the 2-sphere),
- $T^2$ (the torus),
- $T^2 \# T^2$ (the double torus).
:::

:::

:::

::: pf-step
Conclusion:
- **Projective type:** $\mathbb{P}^2, \, 2\mathbb{P}^2, \, 3\mathbb{P}^2, \, 4\mathbb{P}^2, \, 5\mathbb{P}^2$.
- **Torus type:** $S^2, \, T^2, \, T^2 \# T^2$.
:::

:::

:::
