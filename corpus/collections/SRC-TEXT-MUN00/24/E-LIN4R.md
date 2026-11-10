---
schema: qual/card@1
id: E-LIN4R
kind: problem
title: Linear continua in the dictionary order
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
    Read against Munkres, Topology (2000), §24 Exercise 5, printed p. 158; the four sets are
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.5, PDF pp. 4-5. Z+ x [0,1) and [0,1) x [0,1]
    are linear continua, with the least upper bound read off the first coordinate and then
    the fibre; [0,1) x Z+ fails density between 0 x 1 and 0 x 2, and [0,1] x [0,1) fails the
    least upper bound property on the fibre at 1. (tmp/sources/munkres-solutions-positron-
    ch3.pdf).
---

::: {.exercise}

Consider the following sets in the dictionary order.
Which are linear continua?

(a) $\ZZ_+ \times [0, 1)$

(b) $[0, 1) \times \ZZ_+$

(c) $[0, 1) \times [0, 1]$

(d) $[0, 1] \times [0, 1)$
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.5, PDF pp. 4--5** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all four answers and their justifications are theirs.

(a) $\ZZ_{+}\times[0,1)$ **is** a linear continuum. Between $x\times y<z\times w$: if $x=z$ put $(x+y)/2$ in the second coordinate; if $x<z$ take $(x+1)\times0$ if $z=x+1$, and otherwise $(x+1)\times0$ lies strictly between. For the least upper bound property: let $S\ne\varnothing$ be bounded above and put $x=\max\pi_{1}(S)$ (the set of first coordinates is a nonempty subset of the well-ordered $\ZZ_{+}$) and $y=\sup\pi_{2}(S\cap(\{x\}\times[0,1)))$, which exists in $[0,1]$; then $x\times y$ is the least upper bound of $S$ if $y<1$, and $(x+1)\times0$ is if $y=1$.

(b) $[0,1)\times\ZZ_{+}$ **is not**: $0\times1<0\times2$ but there is no element strictly between them, since the first coordinates coincide and no integer lies strictly between $1$ and $2$.

(c) $[0,1)\times[0,1]$ **is** a linear continuum. Density as in (a). For the least upper bound property let $S\ne\varnothing$ be bounded above, put $x=\sup\pi_{1}(S)\le1$; if $x\in\pi_{1}(S)$ then $x\times\sup\pi_{2}(S\cap(\{x\}\times[0,1]))$ is the least upper bound, and if $x\notin\pi_{1}(S)$ then $x\times 0$ is.

(d) $[0,1]\times[0,1)$ **is not**: its element $x\times y$ is not the least upper bound of the fibre $\{x\}\times[0,1)$ relative to the order on the set, since that fibre is bounded above (by $x'\times0$ for $x'>x$) and has no least upper bound in $[0,1]\times[0,1)$.
:::
