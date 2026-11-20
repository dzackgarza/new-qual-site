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
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof has now been located: UC Riverside Math 205A, Fall 2014, Solutions Part 7,
    Munkres §58 Exercise 6, the sheet's p. 5, read in the MinerU extraction
    tmp/sources/ucr-math205A-2014-solutions07.md. The solution is that proof transcribed, with its
    one substantive step written out: the homotopy may be taken to end at a constant map whose
    value lies in $A$, because a contractible space is path connected (§51 Exercise 3(b), printed
    p. 330) and constant maps into a path connected space are homotopic. The source is correct and
    needed no repair; it also notes that $A$ must be nonempty for $a\in A$ to be chosen, which is
    automatic for a retract of a nonempty space. Checked against the book: the exercise on printed
    p. 367, the definition of contractible in §51 Exercise 3 on printed p. 330, and Lemma 51.1 on
    printed p. 324 for the transitivity used to replace the constant value. Not claimed: that the
    source states the pasting or the path-connectedness step in detail -- it writes one sentence
    for each.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, in Lamport form, with the source and
    the book's pages named in its own text.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    Correction to the note of 2026-11-14 above: that note said the UCR sheet "also notes that $A$
    must be nonempty for $a\in A$ to be chosen". It does not. Its solution of §58 Exercise 6, the
    sheet's p. 5, reads "The first thing to notice is that the arcwise connectedness of X implies
    that all constant maps into X are homotopic, and consequently if the identity on X is homotopic
    to a constant map, it is also homotopic to a constant map whose value lies in the subspace A",
    and continues with the composite $h'(a,t)=r\circ H(a,t)$; it never mentions nonemptiness, and
    its argument is stated for $a\in A$ without saying why such an $a$ exists. The nonemptiness
    used on the card is the card's own: a contractible space is nonempty, since the constant map it
    is homotopic to needs a point, and a retraction $X\to\emptyset$ exists only for $X=\emptyset$.
    The rest of that note stands: the sheet's step is the replacement of the constant value by one
    in $A$ through the arcwise connectedness of $X$. Checked against the book: the exercise on
    printed p. 367 and the definition of contractible in §51 Exercise 3 on printed p. 330.
---

::: {.exercise}

Show that a retract of a contractible space is contractible.
:::

::: {.solution}
The exercise is §58 Exercise 6, with *contractible* as recalled
in Exercise 5 of the same list and defined in §51 Exercise 3:
$X$ is contractible when $\operatorname{id}_X$ is nulhomotopic, that is,
homotopic to a constant map.

The proof is transcribed from UC Riverside Math 205A, Fall 2014, Solutions Part
7, Munkres §58 Exercise 6, the sheet's, read in
`tmp/sources/ucr-math205A-2014-solutions07.md`. Its one substantive point is that
the constant map the homotopy ends at may be taken with its value in $A$, so that
composing with the retraction produces a constant map of $A$; that is step
[](#value-in-A){.pf-ref}, and it uses the path connectedness of a contractible
space, which is §51 Exercise 3(b).

::: pf

::: {.pf-step #value-in-A}
$X$ is path connected, $A$ is nonempty, and if $X$ is contractible there is a
homotopy $H:X\times I\to X$ from $\operatorname{id}_X$ to a constant map whose
value lies in $A$.

::: pf-proof
A contractible space is path connected: if $\operatorname{id}_X\simeq c_{x_0}$
by a homotopy $G$, then $t\mapsto G(x,t)$ is a path from $x$ to $x_0$ for each
$x$, and $x_0$ is a point of $X$ since $c_{x_0}$ is a map. $A$ is nonempty: were $A$ empty, the retraction would be a map $r:X\to
\varnothing$, which exists only if $X=\varnothing$, and $X$ is nonempty because
it is contractible. Choose $a\in A$.

By contractibility there is $x\in X$ with $\operatorname{id}_X\simeq c_x$. Since
$X$ is path connected there is a path $\gamma:I\to X$ from $x$ to $a$, and
$(y,t)\mapsto\gamma(t)$ is a homotopy from $c_x$ to $c_a$; by Lemma 51.1
 we get $\operatorname{id}_X\simeq c_a$, and $a\in A$.
:::

:::

::: {.pf-step #composite}
With $H:\operatorname{id}_X\simeq c_a$ as in step [](#value-in-A){.pf-ref}, the
map $h:A\times I\to A$, $h(a',t)=r(H(a',t))$, is a homotopy from
$\operatorname{id}_A$ to a constant map.

::: pf-proof
Since $H$ carries $X\times I$ into $X$ and $r$ maps $X$ into $A$, the map $h$ is
defined and continuous. For $a'\in A$ we have $h(a',0)=r(H(a',0))=r(a')=a'$,
because $r$ is a retraction; and $h(a',1)=r(c_a)=r(a)=a$. So $h$ is a homotopy
from $\operatorname{id}_A$ to the constant map at $a$.
:::

:::

::: {.pf-step}
$\boxed{A\ \text{is contractible}}$.

::: pf-proof
Step [](#composite){.pf-ref} exhibits a homotopy from $\operatorname{id}_A$ to a
constant map of $A$, which is exactly the definition of contractibility on
printed p. 330. So a retract of a contractible space is contractible.
:::

:::

:::
:::
