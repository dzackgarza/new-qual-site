---
schema: qual/card@1
id: E-97HXB
kind: problem
title: Retracts of contractible spaces
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 6, printed p. 366,
    with the definition of contractibility and the composition of homotopies. The card's $K(a,t)=r(H(a,t))$ is the standard nullhomotopy of the identity of $A$, ending at $r(x_0)$. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
---

::: {.exercise}

Show that a retract of a contractible space is contractible.
:::

::: {.solution}
::: pf

::: pf-step
Retraction and contractibility data:

::: pf-proof

::: pf-step
Let $i: A \hookrightarrow X$ be the canonical inclusion map.
:::

::: pf-step
Since $A$ is a retract of $X$, there exists a continuous map $r: X \to A$ such that:
$$r \circ i = \operatorname{id}_A.$$
:::

::: pf-step
Because $X$ is contractible, the identity map $\operatorname{id}_X$ is nullhomotopic: there exists a point $x_0 \in X$ and a continuous homotopy $H: X \times I \to X$ such that:
$$H(x, 0) = x \quad \text{and} \quad H(x, 1) = x_0 \quad \text{for all } x \in X.$$
:::

:::

:::

::: pf-step
Construction of nullhomotopy for $A$:
Define $K: A \times I \to A$ by:
$$K(a, t) = r(H(i(a), t)).$$

::: pf-proof

::: pf-step
The map $K$ is continuous as the composition of continuous maps $r \circ H \circ (i \times \operatorname{id}_I)$.
:::

::: pf-step
At $t = 0$:
$$K(a, 0) = r(H(i(a), 0)) = r(i(a)) = (r \circ i)(a) = a = \operatorname{id}_A(a).$$
:::

::: pf-step
At $t = 1$:
$$K(a, 1) = r(H(i(a), 1)) = r(x_0) \in A.$$
:::

::: pf-step
Setting $a_0 = r(x_0) \in A$, $K(a, 1) = a_0$ is constant for all $a \in A$.
:::

:::

:::

::: pf-step
$K$ is a continuous homotopy between the identity map $\operatorname{id}_A$ and the constant map $c_{a_0}: A \to A$.
Thus $\operatorname{id}_A$ is nullhomotopic, so $A$ is contractible.
:::

:::

:::
