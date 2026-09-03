---
schema: qual/card@1
id: E-WHB87
kind: problem
title: Continuity of composition in the compact-open topology
classification:
  areas:
  - topology
  topics:
  - Function Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Show that if $Y$ is locally compact Hausdorff, then composition of maps

$$
\mathcal{C}(X, Y) \times \mathcal{C}(Y, Z) \to \mathcal{C}(X, Z)
$$

is continuous, provided the compact-open topology is used throughout.
[Hint: If $g \circ f \in S(C, U)$, find $V$ such that $f(C) \subset V$ and $g(\overline{V}) \subset U$.]
:::

::: {.solution}
<1>1. Let $S(C, U) = \{h : h(C) \subseteq U\}$ denote a subbasic open set of the compact-open topology on $\mathcal C(X, Z)$.
::: {.proof}
definition of the compact-open topology.
:::

<1>2. Suppose $g \circ f \in S(C, U)$, i.e. $g(f(C)) \subseteq U$.
::: {.proof}
take a point in a subbasic open set.
:::

<1>3. Since $Y$ is locally compact Hausdorff and $f(C)$ is compact, there is an open set $V$ with $f(C) \subseteq V \subseteq \overline{V}$ and $\overline{V}$ compact, and $g(\overline{V}) \subseteq U$.
::: {.proof}
$f(C)$ is compact; cover it by finitely many open sets with compact closure contained in $g^{-1}(U)$ (using local compactness and the continuity of $g$), and let $V$ be their union.
:::

<1>4. Then $f \in S(C, V)$ and $g \in S(\overline{V}, U)$.
::: {.proof}
$f(C) \subseteq V$ and $g(\overline{V}) \subseteq U$.
:::

<1>5. For any $f' \in S(C, V)$ and $g' \in S(\overline{V}, U)$, we have $g' \circ f' \in S(C, U)$.
::: {.proof}
$f'(C) \subseteq V \subseteq \overline{V}$, so $g'(f'(C)) \subseteq g'(\overline{V}) \subseteq U$.
:::

<1>6. Hence the preimage of $S(C, U)$ under composition contains the open set $S(C, V) \times S(\overline{V}, U)$.
::: {.proof}
<1>4 and <1>5.
:::

<1>7. Therefore composition is continuous.
::: {.proof}
<1>6 shows the preimage of every subbasic open set is open.
:::

<1>8. Q.E.D.
::: {.proof}
<1>7.
:::
:::
