---
schema: qual/card@1
id: E-LVTFA
kind: problem
title: Homotopy equivalence is an equivalence relation
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 3, printed p. 366,
    with the definition of homotopy equivalence. Reflexivity, symmetry and transitivity, the last two by composing with the given homotopies; the card's composites $(gv)(uf)$ and $(uf)(gv)$ are the right ones. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof has now been located: Pearse, *Topology (2nd ed.) — James R. Munkres*,
    solutions, Cornell 2005, §58 Exercise 3, his p. 22, read in the MinerU extraction
    tmp/sources/cornell-erin-munkres.md. The solution is that proof transcribed in Lamport form,
    one step per defining property, with the names of the maps as the source has them. The source
    is correct and needed no repair; it cites §51 Exercise 1 for composing with a homotopic map
    and Lemma 51.1 for transitivity, and the card states both citations with their printed pages.
    Checked against the book: the exercise on printed p. 367, the definition of homotopy
    equivalence and of homotopy inverse on printed p. 363, and the two results cited, §51 Exercise
    1 on printed p. 330 and Lemma 51.1 on printed p. 324. Not claimed: that the book's own remark
    on printed p. 363 ("it is straightforward to show") contains a proof -- it does not, which is
    what the exercise asks for.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, with the source and the book's numbered
    results named in its own text; the earlier proof checked the same three properties in the same
    order and was replaced so that the card carries the published one.
---

::: {.exercise}

Show that given a collection $\mathcal{C}$ of spaces, the relation of homotopy equivalence is an equivalence relation on $\mathcal{C}$.
:::

::: {.solution}
The exercise is §58 Exercise 3, printed p. 367. The proof is transcribed from
Pearse, *Topology (2nd ed.) — James R. Munkres*, solutions, Cornell 2005, §58
Exercise 3, his p. 22, read in `tmp/sources/cornell-erin-munkres.md`: the three
defining properties of an equivalence relation are checked from the book's
definition of homotopy equivalence on printed p. 363, using §51 Exercise 1
(printed p. 330), that a composite of homotopic maps is homotopic, and Lemma
51.1 (printed p. 324), the transitivity of homotopy. Throughout, $f:X\to Y$ and
$g:Y\to X$ are homotopy inverse when $g\circ f\simeq\operatorname{id}_X$ and
$f\circ g\simeq\operatorname{id}_Y$.

::: pf

::: {.pf-step #reflexive}
Every $X\in\mathcal C$ is homotopy equivalent to itself.

::: pf-proof
Take $f=g=\operatorname{id}_X$. Then $g\circ f$ and $f\circ g$ are both
$\operatorname{id}_X$, which is homotopic to itself, so $X$ is homotopy
equivalent to $X$ with homotopy inverse $\operatorname{id}_X$.
:::

:::

::: {.pf-step #symmetric}
If $X$ is homotopy equivalent to $Y$, then $Y$ is homotopy equivalent to $X$.

::: pf-proof
Let $f:X\to Y$ and $g:Y\to X$ satisfy $g\circ f\simeq\operatorname{id}_X$ and
$f\circ g\simeq\operatorname{id}_Y$. The same two homotopies say that $g:Y\to X$
is a homotopy equivalence with homotopy inverse $f$, which is the assertion.
:::

:::

::: {.pf-step #transitive}
If $X$ is homotopy equivalent to $Y$ and $Y$ to $Z$, then $X$ is homotopy
equivalent to $Z$.

::: pf-proof
Let $f:X\to Y$ with inverse $g:Y\to X$, and $h:Y\to Z$ with inverse $k:Z\to Y$.
Consider $h\circ f:X\to Z$ and $g\circ k:Z\to X$. By associativity of
composition,
$$
(g\circ k)\circ(h\circ f)=g\circ(k\circ h)\circ f .
$$
Now $k\circ h\simeq\operatorname{id}_Y$, so composing with $g$ on the left and
$f$ on the right gives $g\circ(k\circ h)\circ f\simeq
g\circ\operatorname{id}_Y\circ f=g\circ f$ by §51 Exercise 1, and
$g\circ f\simeq\operatorname{id}_X$; Lemma 51.1 gives
$(g\circ k)\circ(h\circ f)\simeq\operatorname{id}_X$. The argument for the other
composite is identical: $(h\circ f)\circ(g\circ k)=h\circ(f\circ g)\circ k
\simeq h\circ\operatorname{id}_Y\circ k=h\circ k\simeq\operatorname{id}_Z$, using
$f\circ g\simeq\operatorname{id}_Y$ and $h\circ k\simeq\operatorname{id}_Z$. So
$h\circ f$ is a homotopy equivalence of $X$ with $Z$, and since homotopy
equivalence on the collection $\mathcal C$ is reflexive, symmetric and
transitive, it is an equivalence relation on $\mathcal C$.
:::

:::

:::
:::
