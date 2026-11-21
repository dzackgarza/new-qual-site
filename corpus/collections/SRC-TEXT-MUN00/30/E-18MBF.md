---
schema: qual/card@1
id: E-18MBF
kind: problem
title: Products with a compact factor are Lindelof
classification:
  areas:
  - topology
  topics:
  - Countability
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Ana Emilia Orellana, "Solutions - Topology
    Munkres", Section 30 Exercise 14, printed p. 31
    (tmp/sources/munkres-solutions-anadeore.pdf), checked against Munkres, Topology (2000),
    Section 30 Exercise 14, printed p. 194, and the tube lemma (Lemma 26.8, printed p. 168). Her
    argument: each slice {x} x Y is compact, a finite subcollection covers it, the intersection of
    the finitely many X-coordinates is a neighbourhood U_x of x with U_x x Y covered, and
    Lindelofness of X gives countably many such x. What was corrected: the source then writes the
    countable subcover as the family indexed by those x alone, "U_{x_i n} x V_{x_i n}", which is
    one set per x; the card takes the union of the finitely many members chosen for each x, which
    is what the tube-lemma step produces. The card also settles the empty case X = empty.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card was a label-step with an empty proof over nine nested
    one-sentence claims, and it stated the tube lemma's conclusion without its hypothesis being
    used at the right place. It is now three proved steps: the slice is compact so finitely many
    cover members cover it, and the tube lemma applied to their union gives the tube;
    Lindelöfness of X extracts countably many tubes; and the countable union of the finite
    subcollections is a countable subcover. The empty-space case the card mentions at the start
    is subsumed, an empty space being Lindelöf. Not claimed: a retained solution set; the
    collection's provenance is the Munkres textbook, whose text is not retained here.
---

::: {.exercise}

Show that if $X$ is Lindelöf and $Y$ is compact, then $X \times Y$ is Lindelöf.
:::

::: {.solution}
Throughout $X$ is Lindelöf, $Y$ is compact, and $\mathcal{A}$ is an open cover of $X \times Y$; a space is Lindelöf when every open cover has a countable subcover. The exercise is Munkres, *Topology* (2000), §30.

::: pf

::: {.pf-step #tubes}
For each $x \in X$ there are an open neighbourhood $U_{x}$ of $x$ and a finite subcollection $\mathcal{A}_{x} \subseteq \mathcal{A}$ with $U_{x} \times Y \subseteq \bigcup_{A \in \mathcal{A}_{x}}A$.

::: pf-proof
The slice $\theset{x} \times Y$ is homeomorphic to $Y$ under $y \mapsto (x,y)$, hence compact, and $\mathcal{A}$ covers it; so finitely many $A_{1},\ldots,A_{k} \in \mathcal{A}$ cover $\theset{x}\times Y$. Their union $W_{x}$ is open and contains the slice, so the tube lemma — for a compact factor $Y$ every open set containing $\theset{x}\times Y$ contains a tube $U_{x}\times Y$ — gives an open neighbourhood $U_{x}$ of $x$ with $U_{x}\times Y \subseteq W_{x}$.

:::

:::

::: {.pf-step #countable}
There are $x_{1}, x_{2}, \ldots \in X$ with $X = \bigcup_{n}U_{x_{n}}$.

::: pf-proof
By step [](#tubes){.pf-ref} the sets $U_{x}$, $x \in X$, form an open cover of $X$, and $X$ is Lindelöf, so countably many of them cover $X$.

:::

:::

::: pf-step
$X \times Y$ is Lindelöf.

::: pf-proof
$X \times Y = \bigcup_{n}\bigl(U_{x_{n}} \times Y\bigr)$, and each $U_{x_{n}}\times Y$ is contained in $\bigcup_{A \in \mathcal{A}_{x_{n}}}A$, a union of finitely many members of $\mathcal{A}$ by step [](#tubes){.pf-ref}. Hence the countable subcollection $\bigcup_{n}\mathcal{A}_{x_{n}} \subseteq \mathcal{A}$ covers $X\times Y$; being a countable union of finite sets, it is countable. Every open cover $\mathcal{A}$ therefore has a countable subcover, which is the definition of $X\times Y$ being Lindelöf.

:::

:::

:::
:::
