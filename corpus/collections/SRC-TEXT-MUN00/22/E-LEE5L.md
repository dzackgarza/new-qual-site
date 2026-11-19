---
schema: qual/card@1
id: E-LEE5L
kind: problem
title: A quotient map that is neither open nor closed
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Exercise 3, printed p. 145, with Example 1 of
    §22 for the retraction argument; the subspace A and the two claims are stored as
    printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 22.3, PDF p. 27. The restricted projection is a
    composite of a retraction and a homeomorphism, hence a quotient map; the open half-plane
    in A maps to (0,infinity) and the closed set cut out by the tangent graph maps to an
    open interval, so it is neither open nor closed. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewrote the solution as a Lamport proof and repaired two defects in it. First, the witness that
    q is not open: the image of A cap (R x (0,inf)) is [0,inf), not (0,inf), because the points
    (0,y) with y > 0 lie in A and in that set and have image 0; [0,inf) is still not open in R, so
    the conclusion stands. Re-read the retained set at its own words
    (tmp/sources/positron-ch2.txt, Exercise 22.3): its witness is (R x R_+) cap A with image R_+,
    where R_+ is the non-negative reals in the set A = (R_+ x R) cup (R x {0}) of the exercise, so
    the retained set has [0,inf) and the card's (0,inf) was a transcription slip. Second, the
    witness that q is not closed: the strip pi/2 < x < 3pi/2 is open, not closed, so the stated
    reason C is closed was wrong; C is closed because a convergent sequence of points
    (x_k, tan x_k) has bounded tan x_k, which forces the limit abscissa to lie strictly inside
    (pi/2, 3pi/2), and the step now proves that. Also recorded that C lies in A already, every
    abscissa in it being positive. The statement is unchanged.
---

::: {.exercise}

Let $\pi_1: \RR \times \RR \to \RR$ be projection on the first coordinate.
Let $A$ be the subspace of $\RR \times \RR$ consisting of all points $x \times y$ for which either $x \geq 0$ or $y = 0$ (or both); let $q: A \to \RR$ be obtained by restricting $\pi_1$.
Show that $q$ is a quotient map that is neither open nor closed.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 22.3, PDF p. 27** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the retraction argument and both witnesses are theirs. Write $A=\theset{x\times y\mid x\ge0\text{ or }y=0}\subset\RR^{2}$ and $q=\pi_{1}\restrict_{A}:A\to\RR$.

::: pf

::: {.pf-step #quotient}
$q$ is a quotient map.

::: pf-proof
The retraction $r:A\to\RR\times\{0\}$, $r(x\times y)=x\times0$, is continuous, being the restriction of the continuous map $(x,y)\mapsto x\times0$ of $\RR^{2}$, and it fixes $\RR\times\{0\}$ pointwise, so by Exercise 22.2(b) it is a quotient map. The map $h:\RR\times\{0\}\to\RR$, $h(x\times0)=x$, is a homeomorphism, hence a quotient map. Since $q=h\circ r$, it is a composite of quotient maps, and a composite of quotient maps is a quotient map.
:::

:::

::: {.pf-step #not-open}
$q$ is not an open map.

::: pf-proof
The set $U=(\RR\times(0,\infty))\cap A=\theset{x\times y\mid x\ge0,\ y>0}$ is open in $A$, being the trace on $A$ of the open set $\RR\times(0,\infty)$ of $\RR^{2}$. Its image is $q(U)=[0,\infty)$: every $x\ge0$ occurs as $q(x\times1)$ with $x\times1\in U$, and no $x<0$ occurs because every point of $A$ with a negative abscissa has $y=0$ and so is outside $U$. The set $[0,\infty)$ is not open in $\RR$, since no interval $(-\varepsilon,\varepsilon)$ about $0$ is contained in it. So $q$ carries an open set to a non-open set.
:::

:::

::: {.pf-step #not-closed}
$q$ is not a closed map.

::: pf-proof
Let $C=\theset{x\times\tan x\mid \pi/2<x<3\pi/2}$, a subspace of $\RR^{2}$. It is closed: if $x_{k}\times\tan x_{k}$ converges to $x\times y$ in $\RR^{2}$, then $x_{k}\to x\in[\pi/2,3\pi/2]$ and $\tan x_{k}\to y$ is bounded, and $\abs{\tan t}\to\infty$ as $t$ decreases to $\pi/2$ or increases to $3\pi/2$, so $x$ lies in the open interval $(\pi/2,3\pi/2)$ and $y=\tan x$, giving $x\times y\in C$. Every point of $C$ has positive abscissa, so $C\subset A$ and $C=C\cap A$ is closed in $A$. But $q(C)=(\pi/2,3\pi/2)$, which is not closed in $\RR$, since $\pi/2$ is a limit point of it that it does not contain.
:::

:::

::: {.pf-step #answer}
$q$ is a quotient map that is neither open nor closed.

::: pf-proof
Step [](#quotient){.pf-ref} exhibits $q$ as a quotient map, step [](#not-open){.pf-ref} shows it is not open and step [](#not-closed){.pf-ref} shows it is not closed, which is the assertion of the exercise.
:::

:::

:::
:::
