---
schema: qual/card@1
id: E-MUN-1-10
kind: problem
title: Cartesian products as subsets of $\RR \times \RR$
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 10; the stored statement matches.
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
    Read against Munkres, Topology (2000), §1 Exercise 10, printed p. 15; the five
    subsets (a)-(e) are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.10,
    printed p. 10 (tmp/sources/munkres-solutions-whitman.pdf). His verdicts are the
    card's, and so are the witnesses: for (c) the points (0,1) and (1,2) forcing
    1 to lie in both factors; for (e) the two axis points (0.9,0) and (0,0.9) forcing
    (0.9,0.9) into the product while it lies outside the disc.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the five verdicts, which is what Queue D asks for on this card. The criterion for being a cartesian product is stated and proved as a step of its own, because all three negative verdicts use it; each part is then a step whose justification is a direct coordinate check. The statement was re-read against Munkres, Topology (2000), §1 Exercise 10, printed p. 15, and the verdicts and both witness pairs against Dan Whitman's set, Exercise 1.10, printed p. 10. No statement repair and no change of verdict.
---

::: {.exercise}

Let $\RR$ denote the set of real numbers.
For each of the following subsets of $\RR \times \RR$, determine whether it is equal to the cartesian product of two subsets of $\RR$ .

(a) $\{(x, y) \mid x \text{ is an integer}\}$ .

(b) $\{(x, y) \mid 0 < y \leq 1\}$ .

(c) $\{(x, y) \mid y > x\}$ .

(d) $\{(x, y) \mid x \text{ is not an integer and } y \text{ is an integer}\}$ .

(e) $\{(x, y) \mid x^{2} + y^{2} < 1\}$ .
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.10, printed p. 10** (`tmp/sources/munkres-solutions-whitman.pdf`); the five verdicts and the witnesses for (c) and (e) below are his. The statement is Munkres, *Topology*, 2nd ed. (2000), §1 Exercise 10, printed p. 15.

::: pf

::: {.pf-step #criterion}
A subset $S\subseteq\RR\times\RR$ is a cartesian product $A\times B$ if and only if it is closed under the exchange of coordinates: for all $(x,y),(x',y')\in S$ the point $(x,y')$ also lies in $S$.

::: pf-proof
If $S=A\times B$ and $(x,y),(x',y')\in S$ then $x,x'\in A$ and $y,y'\in B$, so $(x,y')\in A\times B=S$. Conversely, if $S$ has the property, put $A=\{x\mid (x,y)\in S\text{ for some }y\}$ and $B=\{y\mid (x,y)\in S\text{ for some }x\}$; then $S\subseteq A\times B$, and for $(x,y)\in S$ the property applied to $(x,y)$ and $(x',y')\in S$ carrying $x$ gives $(x,y')\in S$, so that $y\in B$ and $(x,y)\in A\times B$; hence $S=A\times B$.
:::

:::

::: {.pf-step #part-a}
(a) Yes: $\{(x,y)\mid x\in\ZZ\}=\ZZ\times\RR$.

::: pf-proof
A point $(x,y)$ has integer first coordinate exactly when $x\in\ZZ$, and its second coordinate is unrestricted in $\RR$; this is the definition of the product $\ZZ\times\RR$. This is the first of the five verdicts.
:::

:::

::: {.pf-step #part-b}
(b) Yes: $\{(x,y)\mid 0<y\le1\}=\RR\times(0,1]$.

::: pf-proof
Membership in the set is decided by the second coordinate alone, through the condition $0<y\le1$ that defines the interval $(0,1]$, and no condition is placed on $x$.
:::

:::

::: {.pf-step #part-c}
(c) No: $\{(x,y)\mid y>x\}$ is not a cartesian product.

::: pf-proof
The points $(0,1)$ and $(1,2)$ both satisfy $y>x$, so if the set were $A\times B$ then $0,1\in A$ and $1,2\in B$. Then $(1,1)\in A\times B$, but $1>1$ is false, so $(1,1)$ is not in the set: a contradiction with the criterion of step [](#criterion){.pf-ref}.
:::

:::

::: {.pf-step #part-d}
(d) Yes: $\{(x,y)\mid x\notin\ZZ,\ y\in\ZZ\}=(\RR-\ZZ)\times\ZZ$.

::: pf-proof
Here membership is decided coordinatewise and separately, by $x\in\RR-\ZZ$ and $y\in\ZZ$, which is exactly the definition of the product of those two sets.
:::

:::

::: {.pf-step #part-e}
(e) No: the open unit disc $\{(x,y)\mid x^2+y^2<1\}$ is not a cartesian product.

::: pf-proof
The points $(0.9,0)$ and $(0,0.9)$ lie in the disc, since $0.9^2+0^2=0.81<1$. If the disc were $A\times B$ then $0.9,0\in A$ and $0,0.9\in B$, so by the criterion of step [](#criterion){.pf-ref} the point $(0.9,0.9)$ would lie in the disc; but $0.9^2+0.9^2=1.62>1$. So the disc is not a product, and the five verdicts are (a), (b), (d) yes and (c), (e) no.
:::

:::

:::
:::
