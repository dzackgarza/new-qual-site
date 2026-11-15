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
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §46 Exercise 7 (printed p. 289) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against Theorem 46.10 (the compact-open topology
    is admissible for locally compact Hausdorff Y) and the definition of the compact-open subbasis in §46. The
    proof is the exercise's hint, made explicit: since g^{-1}(U) is an open set containing the compact set
    f(C), and Y is locally compact Hausdorff (hence regular), each point of f(C) has an open neighbourhood with
    compact closure inside g^{-1}(U), finitely many of which cover f(C); their union V has compact closure in
    g^{-1}(U), so S(C,V) x S(closure V, U) is a neighbourhood of (f,g) mapped into S(C,U) by composition.
    Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Math StackExchange 832519, "Munkres page 289 #7"
    (2014-06-13), is this exercise, and its accepted answer 832867 by Daniel Fischer supplies the step
    the hint leaves open: for the compact set K = f(C) inside the open set W = g^{-1}(U), each y in K
    has a compact neighbourhood contained in W, since Y is locally compact Hausdorff; finitely many
    interiors V_y cover K, and V their union has closure in W. That is step 1 of the card, and the
    card's argument agrees with it, including the use of local compactness through the existence of a
    compact neighbourhood inside a given open set. Nothing needed correction. The AoPS blog post by
    cinnamon_e, "Topology by Munkres Chapter 7 | Day 17" (2025-09-10,
    https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), also answers the exercise at its item 7 of
    §46 with its formulas lost; the queries of this pass are in the COMPLAINTS.md entry for
    §43--§50.
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

::: pf

::: {.pf-step #s1}

If $g(f(C)) \subseteq U$, there is an open $V \subseteq Y$ with $f(C) \subseteq V$, $\overline{V}$ compact, and $g(\overline{V}) \subseteq U$.

::: pf-proof

The set $g^{-1}(U)$ is open and contains the compact set $f(C)$. Since $Y$ is locally compact Hausdorff, each $y \in f(C)$ has an open neighborhood $W_y$ with $\overline{W_y}$ compact and $\overline{W_y} \subseteq g^{-1}(U)$. Finitely many $W_{y_1}, \ldots, W_{y_k}$ cover $f(C)$; put $V = W_{y_1} \cup \cdots \cup W_{y_k}$. Then $\overline{V} = \overline{W_{y_1}} \cup \cdots \cup \overline{W_{y_k}}$ is compact and contained in $g^{-1}(U)$.

:::

:::

::: {.pf-step #s2}

$S(C, V) \times S(\overline{V}, U)$ is an open neighborhood of $(f, g)$ whose image under composition lies in $S(C, U)$.

::: pf-proof

By step [](#s1){.pf-ref}, $f(C) \subseteq V$ and $g(\overline{V}) \subseteq U$, and $\overline{V}$ is compact, so $(f, g) \in S(C, V) \times S(\overline{V}, U)$, a product of subbasic open sets. If $f' \in S(C, V)$ and $g' \in S(\overline{V}, U)$, then $g'(f'(C)) \subseteq g'(\overline{V}) \subseteq U$.

:::

:::

::: pf-qed

By step [](#s2){.pf-ref}, the preimage of every subbasic open set of $\mathcal C(X, Z)$ is open, so composition is continuous.

:::

:::

:::
