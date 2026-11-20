---
schema: qual/card@1
id: E-6RQWT
kind: problem
title: Contractibility and the one-point homotopy type
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
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 5, printed p. 366,
    with the definition of contractibility and of homotopy equivalence. Both directions: a contraction is a homotopy from the identity to a constant, which is the composite through the one-point space, and conversely a homotopy inverse to the collapse to a point makes the identity nullhomotopic. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof has now been located: Harvard Math 131 (2000-01), Solution Set 10, item
    9.58.5, on the second page of the set, read in the MinerU extraction
    tmp/sources/harvard131-soln10.md. The solution transcribes it in both directions with the maps
    written out. The source contains one slip, now named on the card: for the direction from the
    homotopy type of a point it writes the composite as $f\circ g$ and says that composite is
    constant; with $f:X\to\theset y$ and $g:\theset y\to X$ the composite with source $X$ is
    $g\circ f$, and $f\circ g$ is a self-map of the point. Read as $g\circ f$ the argument is
    correct, and the card states it that way rather than repeating the slip. Checked against the
    book: the exercise and its recalled definition on printed p. 367, the definition of
    contractible in §51 Exercise 3 on printed p. 330, and the definition of homotopy equivalence
    and homotopy inverse on printed p. 363. Not claimed: that the set states which composite it
    means -- it does not, and the conclusion it draws fixes the reading.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, in Lamport form, with the source, the
    slip and the book's pages named in its own text.
---

::: {.exercise}

Recall that a space $X$ is said to be contractible if the identity map of $X$ to itself is nulhomotopic.
Show that $X$ is contractible if and only if $X$ has the homotopy type of a one-point space.
:::

::: {.solution}
The exercise is §58 Exercise 5. The proof is transcribed from
Harvard Math 131 (2000--01), Solution Set 10, item 9.58.5, on the second page of
the set, read in `tmp/sources/harvard131-soln10.md`: each direction is one line
there, and the card writes out the maps and the two composites.

One correction to the source. For the direction "homotopy type of a point
implies contractible" it writes that there are maps $f:X\to y$ and $g:y\to X$
with $f\circ g\simeq 1_X$, and that $f\circ g$ is constant. The composite that
has source $X$ is $g\circ f$, not $f\circ g$: with $f:X\to\theset y$ and
$g:\theset y\to X$, the map $f\circ g$ is a self-map of the one-point space,
while $g\circ f$ is the constant self-map of $X$ at $g(y)$, and only the latter
gives the conclusion. With $g\circ f$ read in place of $f\circ g$ the argument is
correct, and step [](#backward){.pf-ref} states it that way.

Notation. $X$ is contractible when $\operatorname{id}_X$ is nulhomotopic
(§51 Exercise 3), and $X$ has the homotopy type of a one-point
space when there are a one-point space $\theset y$ and maps $f:X\to\theset y$,
$g:\theset y\to X$ with $g\circ f\simeq\operatorname{id}_X$ and
$f\circ g\simeq\operatorname{id}_{\theset y}$ (definition of homotopy inverse, §58).

::: pf

::: {.pf-step #forward}
If $X$ is contractible, then $X$ has the homotopy type of a one-point space.

::: pf-proof
Let $\operatorname{id}_X\simeq c_{x_0}$ for some $x_0\in X$, and put
$Y=\theset{x_0}$. Let $f:X\to Y$ be the only map, so $f=c_{x_0}$, and let
$g:Y\to X$ be the inclusion. Then $g\circ f=c_{x_0}\simeq\operatorname{id}_X$ by
hypothesis, and $f\circ g$ is the only self-map of $Y$, hence
$\operatorname{id}_Y$. So $f$ and $g$ are homotopy inverse and $X$ has the
homotopy type of the one-point space $Y$.
:::

:::

::: {.pf-step #backward}
If $X$ has the homotopy type of a one-point space, then $X$ is contractible.

::: pf-proof
Let $Y=\theset y$ and let $f:X\to Y$, $g:Y\to X$ satisfy
$g\circ f\simeq\operatorname{id}_X$. Put $x_0=g(y)$, the only value of $g$. For
every $x\in X$ we have $f(x)=y$, so $(g\circ f)(x)=g(y)=x_0$; thus $g\circ f$ is
the constant map $c_{x_0}$, and $\operatorname{id}_X\simeq c_{x_0}$. By the
definition of contractibility in §52 this is the assertion.
:::

:::

::: {.pf-step}
$\boxed{X\ \text{is contractible}\iff X\ \text{has the homotopy type of a
one-point space}}$.

::: pf-proof
Step [](#forward){.pf-ref} gives one implication and step [](#backward){.pf-ref}
the other. The argument of step [](#forward){.pf-ref} also shows that a
contractible space is nonempty, since a constant map $X\to X$ has a value
$x_0\in X$.
:::

:::

:::
:::
