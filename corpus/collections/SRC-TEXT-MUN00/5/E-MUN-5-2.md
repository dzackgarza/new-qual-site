---
schema: qual/card@1
id: E-MUN-5-2
kind: problem
title: Associativity of finite and infinite Cartesian products
classification:
  areas:
  - topology
  topics:
  - Cartesian Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 5, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §5 Exercise 2, printed p. 38; both parts
    are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 5.2,
    printed pp. 68-69 (tmp/sources/munkres-solutions-whitman.pdf). His (a) splits at the
    last coordinate and his (b) is the pairing map (a_1,a_2,a_3,...) -> ((a_1,a_2),
    (a_3,a_4), ...); the card gives the same two maps with the inverse written directly,
    which is what proves bijectivity, rather than his coordinate-by-coordinate injectivity
    and surjectivity checks. His parity lemma (that i/2 or (i+1)/2 is a positive integer
    according as i is even or odd) is what the card's appeal to the displayed inverse
    replaces.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the finite case with its map and inverse,
    the infinite case with the pairing map, its being into the product of the B_i, and its
    inverse. The two bijections are the retained solution's; its cited pages were not re-read
    in this pass, and the printed statement was not re-read either.
---

::: {.exercise}

(a) Show that if $n > 1$ there is bijective correspondence of
$$
A_{1} \times \dots \times A_{n} \quad \text{with} \quad (A_{1} \times \dots \times A_{n-1}) \times A_{n}.
$$

(b) Given the indexed family $\{A_{1}, A_{2}, \ldots\}$, let $B_{i} = A_{2i-1} \times A_{2i}$ for each positive integer $i$. Show there is bijective correspondence of $A_{1} \times A_{2} \times \cdots$ with $B_{1} \times B_{2} \times \cdots$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 5.2, printed pp. 68--69** (`tmp/sources/munkres-solutions-whitman.pdf`); the two bijections are his, and where he checks injectivity and surjectivity coordinate by coordinate the card exhibits the two-sided inverse.

::: pf

::: {.pf-step #finite}
(a) For $n>1$ there is a bijection $A_{1}\times\cdots\times A_{n}\to(A_{1}\times\cdots\times A_{n-1})\times A_{n}$.

::: pf-proof
The map and a two-sided inverse.

::: {.pf-step #phi}
$\Phi(a_{1},\dots,a_{n})=\bigl((a_{1},\dots,a_{n-1}),a_{n}\bigr)$ is a well-defined map of the two products.

::: pf-proof
An element of $A_{1}\times\cdots\times A_{n}$ is a function $a$ on $\{1,\dots,n\}$ with $a_{i}\in A_{i}$; the rule assigns to it the pair whose first entry is the restriction of $a$ to $\{1,\dots,n-1\}$, an element of $A_{1}\times\cdots\times A_{n-1}$, and whose second entry is $a_{n}\in A_{n}$. So the values lie in the target, and the rule is a function of $a$ alone.
:::

:::

::: {.pf-step #phi-inverse}
$\Phi$ has the two-sided inverse $\bigl((a_{1},\dots,a_{n-1}),a_{n}\bigr)\mapsto(a_{1},\dots,a_{n})$.

::: pf-proof
Composing $\Phi$ with the displayed rule returns $(a_{1},\dots,a_{n})$ on the product of the $A_{1},\dots,A_{n}$, and composing in the other order returns $\bigl((a_{1},\dots,a_{n-1}),a_{n}\bigr)$ on $(A_{1}\times\cdots\times A_{n-1})\times A_{n}$; both composites are the identity on their domains. A map with a two-sided inverse is a bijection, so the two products in (a) are in bijective correspondence.
:::

:::

:::

:::

::: {.pf-step #infinite}
(b) With $B_{i}=A_{2i-1}\times A_{2i}$, the product $A_{1}\times A_{2}\times\cdots$ is in bijective correspondence with $B_{1}\times B_{2}\times\cdots$.

::: pf-proof
The pairing map, its target, and its inverse.

::: {.pf-step #psi-into}
$\Psi(a_{1},a_{2},a_{3},a_{4},\dots)=\bigl((a_{1},a_{2}),(a_{3},a_{4}),\dots\bigr)$ is a well-defined map into $\prod_{i\ge1}B_{i}$.

::: pf-proof
An element of $\prod_{j\ge1}A_{j}$ is a sequence $a$ with $a_{j}\in A_{j}$ for every $j$. Its $i$-th pair is $(a_{2i-1},a_{2i})\in A_{2i-1}\times A_{2i}=B_{i}$, so the rule assigns to $a$ an element of $\prod_{i\ge1}B_{i}$.
:::

:::

::: {.pf-step #psi-inverse}
Flattening the pairs, $\bigl((b_{1},b_{2}),(b_{3},b_{4}),\dots\bigr)\mapsto(b_{1},b_{2},b_{3},b_{4},\dots)$, is a two-sided inverse to $\Psi$.

::: pf-proof
Given $b\in\prod_{i\ge1}B_{i}$, each $b$ evaluated at an odd index is a pair whose entries lie in the corresponding $A$-factors, so the flattened sequence is an element of $\prod_{j\ge1}A_{j}$; flattening after pairing returns $b$, and pairing after flattening returns $a$, since the $2i-1$-st and $2i$-th coordinates of $a$ are exactly the $i$-th pair. Hence $\Psi$ is a bijection and the two infinite products are in bijective correspondence.
:::

:::

:::

:::

:::
:::
