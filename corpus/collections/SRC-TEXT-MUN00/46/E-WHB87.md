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
For compact $C$ and open $U$, write $S(C, U) = \{h : h(C) \subseteq U\}$; these sets form a subbasis of the compact-open topology. It suffices to show that every point $(f, g)$ of the preimage of a subbasic set $S(C, U) \subseteq \mathcal C(X, Z)$ under composition has a neighborhood inside that preimage.

<1>1. If $g(f(C)) \subseteq U$, there is an open $V \subseteq Y$ with $f(C) \subseteq V$, $\overline{V}$ compact, and $g(\overline{V}) \subseteq U$.

::: {.proof}
The set $g^{-1}(U)$ is open and contains the compact set $f(C)$. Since $Y$ is locally compact Hausdorff, each $y \in f(C)$ has an open neighborhood $W_y$ with $\overline{W_y}$ compact and $\overline{W_y} \subseteq g^{-1}(U)$. Finitely many $W_{y_1}, \ldots, W_{y_k}$ cover $f(C)$; put $V = W_{y_1} \cup \cdots \cup W_{y_k}$. Then $\overline{V} = \overline{W_{y_1}} \cup \cdots \cup \overline{W_{y_k}}$ is compact and contained in $g^{-1}(U)$.
:::

<1>2. $S(C, V) \times S(\overline{V}, U)$ is an open neighborhood of $(f, g)$ whose image under composition lies in $S(C, U)$.

::: {.proof}
By step <1>1, $f(C) \subseteq V$ and $g(\overline{V}) \subseteq U$, and $\overline{V}$ is compact, so $(f, g) \in S(C, V) \times S(\overline{V}, U)$, a product of subbasic open sets. If $f' \in S(C, V)$ and $g' \in S(\overline{V}, U)$, then $g'(f'(C)) \subseteq g'(\overline{V}) \subseteq U$.
:::

<1>3. Q.E.D.

::: {.proof}
By step <1>2, the preimage of every subbasic open set of $\mathcal C(X, Z)$ is open, so composition is continuous.
:::
:::
