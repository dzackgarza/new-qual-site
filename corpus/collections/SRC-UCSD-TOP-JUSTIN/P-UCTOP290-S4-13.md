---
schema: qual/card@1
id: P-UCTOP290-S4-13
kind: problem
title: Six-sheeted cover from a free-group map to $S_3$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-corrected
  by: chatgpt
  date: 2026-10-31
  note: >-
    Sheet 4, Problem 13 says the kernel is a subgroup of S3, but the
    displayed map has domain F2. The kernel is a subgroup of F2.
    Read the statement against the extraction and PDF page image.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 4, problem 13
    (assets/attachments/UCSD_290_F14_sheet4.pdf, printed page 254), from the
    checked-in extraction and a 300 dpi render. The printed problem asks for the
    cover corresponding to "the subgroup H of the symmetric group S_3 which is
    the kernel of the map F_2 -> S_3 given by sending a |-> (12) and
    b |-> (123)". The kernel of a map out of F_2 is a subgroup of F_2, not of
    S_3, so the printed identification of H is wrong and the card's statement,
    which puts the kernel in F_2, is the repaired form; the repair was already
    recorded by an earlier source-corrected event and is confirmed here against
    the printed words. The displayed map, (12) and (123), is as the card states.
---

::: {.problem}
Let $F_2=\pi_1(S^1\vee S^1)=\langle a,b\rangle$.
Let $\phi:F_2\to S_3$ send $a$ to $(12)$ and $b$ to $(123)$.
Construct the covering space corresponding to $\ker\phi$.
:::

::: {.solution}

Let $F_2=\langle a,b\rangle=\pi_1(S^1\vee S^1)$ and let $\phi\colon F_2\to
S_3$ send $a\mapsto(12)$ and $b\mapsto(123)$; write $\phi$ on the right, so
that a word $w$ of length $r$ is sent to a product of $r$ permutations.

::: pf

::: {.pf-step #cover}

The labelled graph with one vertex for each $g\in S_3$, an $a$-edge $g\to
g(12)$ and a $b$-edge $g\to g(123)$ at every vertex, is a connected
six-sheeted covering of $S^1\vee S^1$.

::: pf-proof

For a fixed permutation $\sigma$, right multiplication $g\mapsto g\sigma$ is a
bijection of $S_3$ with inverse $g\mapsto g\sigma^{-1}$, so each vertex has
exactly one incoming and one outgoing edge of each label, which is the
covering condition; distinct labels give distinct edges, so there are twelve
edges and six vertices. The two permutations $(12)$ and $(123)$ generate
$S_3$, so from the identity vertex every vertex is reachable by a labelled
path, and the graph is connected.

:::

:::

::: {.pf-step #subgroup}

The subgroup of this cover at the identity vertex $e$ is exactly $\ker\phi$.

::: pf-proof

Right multiplication is an action of $S_3$ on itself, so the vertex reached by
a word $w$ from $e$ is the product of the permutations that $w$'s letters
name, that is $\phi(w)$. A based loop at $e$ is a word that returns to $e$, so
the loops are exactly the words with $\phi(w)=e$. Reading a lifted loop down
in $S^1\vee S^1$ returns the word, and a covering map injects on fundamental
groups, so the subgroup is $\ker\phi$.

:::

:::

::: {.pf-step #deck}

The cover is regular, its deck group is $S_3$ acting by left multiplication on
the vertex labels, and $\ker\phi$ has index $6$ and rank $7$.

::: pf-proof

$\ker\phi$ is a kernel, hence normal, and $F_2/\ker\phi\cong S_3$ by the first
isomorphism theorem, so the cover is regular with deck group the quotient
$F_2/\ker\phi$; the quotient acts on the cosets, which are the vertices, by
left multiplication, and left multiplication by a non-identity element moves
every vertex, so the action is faithful. The graph has six vertices and twelve
edges, so the rank is $1-6+12=7$, matching $1+6(2-1)$ for a six-sheeted cover
of a wedge of two circles.

:::

:::

:::


:::
