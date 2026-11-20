---
schema: qual/card@1
id: E-U00IE
kind: problem
title: Well-ordered sets times the half-open interval are linear continua
classification:
  areas:
  - topology
  topics:
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 6, printed p. 158; the stored
    statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.6, PDF p. 5. Density by the midpoint in the
    second coordinate, and the least upper bound property through the greatest lower bound
    property: the least first coordinate of a set bounded below exists by well-ordering, and
    the fibre over it has a greatest lower bound in [0,1). (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

Show that if $X$ is a well-ordered set, then $X \times [0, 1)$ in the dictionary order is a linear continuum.
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.6** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs, with the greatest-lower-bound verification written out in its two cases.

Let $X$ be well ordered and let $L=X\times[0,1)$ carry the dictionary order; write $x\times t$ for an element, and let $\pi_{1}$ be the first projection.

::: pf

::: {.pf-step #dense}
$L$ has no gaps: between any two elements there is a third.

::: pf-proof
Let $x\times y<z\times w$. If $x=z$ then $y<w$ and $x\times\frac{y+w}{2}$ satisfies $x\times y<x\times\frac{y+w}{2}<x\times w$, with $\frac{y+w}{2}\in[0,1)$ because $y<\frac{y+w}{2}<w<1$. If $x<z$ then $\frac{y+1}{2}\in(y,1)\subseteq[0,1)$ and $x\times y<x\times\frac{y+1}{2}<z\times w$, the outer inequalities holding because the first coordinates satisfy $x=x<z$.
:::

:::

::: {.pf-step #glb}
Every nonempty subset $S\subseteq L$ that is bounded below has a greatest lower bound.

::: pf-proof
$\pi_{1}(S)$ is a nonempty subset of the well-ordered set $X$, so it has a least element $x_{0}$; by definition of $\pi_{1}(S)$ the set $T=\theset{t\in[0,1)\mid x_{0}\times t\in S}$ is nonempty, and it is bounded below by $0$, so it has a greatest lower bound $y_{0}$ in $\RR$, which lies in $[0,1)$. Put $b=x_{0}\times y_{0}$. For $z\times w\in S$ one has $z\ge x_{0}$; if $z=x_{0}$ then $w\in T$ so $w\ge y_{0}$ and $z\times w\ge b$, while if $z>x_{0}$ then $z\times w>b$ by the dictionary order. So $b$ is a lower bound of $S$. If $u\times v<b$ were a lower bound of $S$, then either $u<x_{0}$, which makes $u$ a lower bound of $\pi_{1}(S)$ and contradicts the minimality of $x_{0}$, or $u=x_{0}$ and $v<y_{0}$, which makes $v$ a lower bound of $T$ and contradicts the definition of $y_{0}$. So $b$ is the greatest lower bound.
:::

:::

::: {.pf-step #lub}
Every nonempty subset $S\subseteq L$ that is bounded above has a least upper bound.

::: pf-proof
Reversing the order of a simply ordered set exchanges least upper bounds with greatest lower bounds, so the greatest-lower-bound property of step [](#glb){.pf-ref} is equivalent to the least-upper-bound property.
:::

:::

::: {.pf-qed}
$L$ is a simply ordered set with the least upper bound property and with more than one point, and it is dense by step [](#dense){.pf-ref}; those are the two conditions defining a linear continuum (§24). So $X\times[0,1)$ in the dictionary order is a linear continuum.
:::

:::

:::
