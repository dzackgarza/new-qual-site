---
schema: qual/card@1
id: E-MUN-3-8
kind: problem
title: Ordering the real line by absolute value
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Example 7 and Exercise 8, printed p. 29.
    Example 7 defines xCy iff x^2 < y^2, or x^2 = y^2 and x < y, and says "you can check
    that this is an order relation"; Exercise 8 asks for that check. The stored
    statement matches, and the definition is stated on the card so that the exercise
    stands alone.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.8,
    printed p. 27 (tmp/sources/munkres-solutions-whitman.pdf). His three checks are the
    ones below; the remark that the order differs from the usual one, with -2 and 1 as
    witnesses, is his.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, transcribing the cited published solution: Dan Whitman,
    Topology, Second Edition by James Munkres: Solutions Manual (2019), Exercise 3.8, printed p. 27.
    Checked against Munkres §3 Example 7 and Exercise 8, whose number is read from the collection
    index. Each step re-read: nonreflexivity fails both alternatives of the definition;
    comparability splits into distinct squares, where totality of the order on R applies, and
    equal squares with x != y, where (x-y)(x+y) = 0 gives y = -x and the sign of x decides; and
    transitivity is the four-case analysis, both alternatives of the first hypothesis against both
    of the second. The closing comparison (-2 < 1 but 1C(-2)) is kept. Not claimed: any statement
    about whether C is a well-order, which it is not, R having no least element under it.
---

::: {.exercise}

Check that the relation defined in Example 7 is an order relation; that is, define $xCy$ if $x^2 < y^2$, or if $x^2 = y^2$ and $x < y$, and show that $C$ is an order relation on the real line.
:::

::: {.solution}
The argument is transcribed from the published solution of Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.8, printed p. 27 (`tmp/sources/munkres-solutions-whitman.pdf`); the three checks and the closing comparison with the usual order are his. It is checked against Munkres, Topology (2000), §3 Example 7 and Exercise 8.

::: pf

::: {.pf-step #definition}
Define $xCy$ to mean $x^{2}<y^{2}$, or $x^{2}=y^{2}$ with $x<y$.

::: pf-proof
This is the relation of Example 7; an order relation is required to be nonreflexive, transitive and comparable, which are steps [](#nonreflexive){.pf-ref}, [](#transitive){.pf-ref} and [](#comparable){.pf-ref}.
:::

:::

::: {.pf-step #nonreflexive}
Not $xCx$ for any real $x$.

::: pf-proof
Both alternatives of step [](#definition){.pf-ref} fail: $x^{2}<x^{2}$ is false, and the second alternative requires $x<x$.
:::

:::

::: {.pf-step #comparable}
For $x\ne y$, either $xCy$ or $yCx$.

:::: pf-proof

::: {.pf-step #squaresdistinct}
If $x^{2}\ne y^{2}$ then one of $x^{2}<y^{2}$, $y^{2}<x^{2}$ holds.

::: pf-proof
The order on $\RR$ is total, so two distinct real numbers compare.
:::

:::

::: {.pf-step #squaresequal}
If $x^{2}=y^{2}$ and $x\ne y$ then $y=-x\ne0$, and either $x<y$ or $y<x$.

::: pf-proof
$x^{2}=y^{2}$ gives $(x-y)(x+y)=0$, and $x\ne y$ forces $x+y=0$, so $y=-x$ and $x\ne0$. If $x>0$ then $y=-x<0<x$, so $y<x$; if $x<0$ then $x<0<-x=y$, so $x<y$.
:::

:::

:::

:::

::: {.pf-step #transitive}
If $xCy$ and $yCz$ then $xCz$.

::: pf-proof
Four cases. If $x^{2}<y^{2}$ and $y^{2}<z^{2}$ then $x^{2}<z^{2}$. If $x^{2}<y^{2}$ and $y^{2}=z^{2}$ then $x^{2}<z^{2}$. If $x^{2}=y^{2}$ with $x<y$ and $y^{2}<z^{2}$ then $x^{2}<z^{2}$. If $x^{2}=y^{2}$ with $x<y$ and $y^{2}=z^{2}$ with $y<z$, then $x^{2}=z^{2}$ and $x<y<z$. In every case $xCz$ by step [](#definition){.pf-ref}.
:::

:::

::: {.pf-step #order}
$C$ is an order relation on $\RR$.

::: pf-proof
Steps [](#nonreflexive){.pf-ref}, [](#transitive){.pf-ref} and [](#comparable){.pf-ref} are the three defining properties. The relation is not the usual order: $-2<1$ but $1^{2}=1<4=(-2)^{2}$, so $1C(-2)$ and not $(-2)C1$, which is the content of the example:
$$
\boxed{C\text{ is an order relation on }\RR,\text{ and it is not the usual order.}}
$$
:::

:::

:::
:::
