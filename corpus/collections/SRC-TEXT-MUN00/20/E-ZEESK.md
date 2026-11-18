---
schema: qual/card@1
id: E-ZEESK
kind: problem
title: The metric is continuous exactly for its own topology
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §20 Exercise 3, printed p. 126; both parts are
    stored as printed, including the summary sentence printed there.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 20.3, PDF pp. 17-18. The metric on X x X is
    continuous by the epsilon-neighbourhood argument from the triangle inequality, and
    continuity of d on X' x X' makes every ball B_d(x, epsilon) the preimage of a half-line
    under a separately continuous map, so the topology of X' contains that of X.
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and checked both parts against Munkres §20 Exercise 3,
    printed p. 122: continuity of d by the two triangle-inequality bounds on a product of
    balls around a point of the preimage of an interval, with the bounded open intervals as
    a basis of R; and the finer topology through the imbedding y -> (x,y) of §18 Exercise 4
    and B_d(x,epsilon) = h^{-1}((-infinity,epsilon)). positron0802, Exercise 20.3, PDF pp.
    17-18; Whitman, printed p. 205. The printed statement needed no repair.
---

::: {.exercise}

Let $X$ be a metric space with metric $d$.

(a) Show that $d: X \times X \to \RR$ is continuous.

(b) Let $X'$ denote a space having the same underlying set as $X$.
Show that if $d: X' \times X' \to \RR$ is continuous, then the topology of $X'$ is finer than the topology of $X$.

One can summarize the result of this exercise as follows: if $X$ has a metric $d$, then the topology induced by $d$ is the coarsest topology relative to which the function $d$ is continuous.
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.3, PDF pp. 17--18** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both parts are theirs, and Whitman, printed p. 205, argues the same two points.

::: pf

::: {.pf-step #part-a}
(a) $d:X\times X\to\RR$ is continuous.

:::: pf-proof

::: {.pf-step #preimage-interval}
For every bounded open interval $(a,b)\subset\RR$, the set $d^{-1}\big((a,b)\big)$ is open in $X\times X$.

::: pf-proof
Let $(x,y)\in d^{-1}\big((a,b)\big)$ and put $r=d(x,y)$, so $a<r<b$; choose $\varepsilon>0$ with $r-2\varepsilon>a$ and $r+2\varepsilon<b$, for instance $\varepsilon=\tfrac13\min\{r-a,b-r\}$. $$
(x,y)\in B_{d}(x,\varepsilon)\times B_{d}(y,\varepsilon)\subset d^{-1}\big((a,b)\big).
$$
Let $(w,z)$ lie in that product, so $d(x,w)<\varepsilon$ and $d(y,z)<\varepsilon$. Then
$$
d(w,z)\le d(w,x)+d(x,y)+d(y,z)<r+2\varepsilon<b
$$
by the triangle inequality twice, and from $d(x,y)\le d(x,w)+d(w,z)+d(z,y)$,
$$
a<r-2\varepsilon=d(x,y)-d(x,w)-d(y,z)\le d(w,z).
$$
So $a<d(w,z)<b$ and $(w,z)\in d^{-1}\big((a,b)\big)$. The product of two open balls is a basis element of $X\times X$ containing $(x,y)$, so $d^{-1}\big((a,b)\big)$ is open.
:::

:::

::: {.pf-step}
(a) holds.

::: pf-proof
The bounded open intervals form a basis of $\RR$, and $d^{-1}$ preserves unions, so the preimage under $d$ of an arbitrary open set of $\RR$ is a union of sets of the form $d^{-1}\big((a,b)\big)$, each open by step [](#preimage-interval){.pf-ref}. Hence the preimage of every open set is open and $d$ is continuous (Theorem 18.1).
:::

:::

:::

:::

::: {.pf-step #part-b}
(b) If $X'$ has the same underlying set as $X$ and $d:X'\times X'\to\RR$ is continuous, then the topology of $X'$ is finer than the topology of $X$.

::: pf-proof
Fix $x\in X'$. The map $h(y)=d(x,y)$ is the composite of the continuous map $d$ with the imbedding $y\mapsto(x,y)$ of $X'$ into $X'\times X'$ (Munkres §18 Exercise 4), so $h$ is continuous. For $\varepsilon>0$,
$$
B_{d}(x,\varepsilon)=\{y\in X'\mid d(x,y)<\varepsilon\}=h^{-1}\big((-\infty,\varepsilon)\big)
$$
is the preimage of an open subset of $\RR$ under $h$, hence open in $X'$. The balls $B_{d}(x,\varepsilon)$ form a basis for the topology of $X$ that $d$ induces, so that topology is contained in the topology of $X'$, that is, the topology of $X'$ is finer.
:::

:::

::: {.pf-step}
Both parts hold, so the topology induced by $d$ is the coarsest topology on $X$ relative to which $d$ is continuous.

::: pf-proof
Step [](#part-a){.pf-ref} shows that $d$ is continuous for the topology it induces, and step [](#part-b){.pf-ref} shows that every topology making $d$ continuous is finer than that one; so the induced topology is the coarsest such topology.
:::

:::

:::
:::
