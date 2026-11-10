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
---

::: {.exercise}

Let $X$ be a metric space with metric $d$.

(a) Show that $d: X \times X \to \RR$ is continuous.

(b) Let $X'$ denote a space having the same underlying set as $X$.
Show that if $d: X' \times X' \to \RR$ is continuous, then the topology of $X'$ is finer than the topology of $X$.

One can summarize the result of this exercise as follows: if $X$ has a metric $d$, then the topology induced by $d$ is the coarsest topology relative to which the function $d$ is continuous.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.3, PDF pp. 17--18** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both parts are theirs. Whitman's printed p. 205 argues the same two points.

(a) It is enough to show that $d^{-1}((a,b))$ is open in $X\times X$ for every bounded open interval $(a,b)\subset\RR$, since those intervals form a basis of $\RR$ and $d^{-1}$ preserves unions. Let $x\times y\in d^{-1}((a,b))$, so $a<r<b$ where $r=d(x,y)$. Choose $\varepsilon>0$ with $a<r-2\varepsilon$ and $r+2\varepsilon<b$. We claim
$$
x\times y\in B_{d}(x,\varepsilon)\times B_{d}(y,\varepsilon)\subset d^{-1}((a,b)).
$$
Let $w\times z$ be a point of that product, so $d(x,w)<\varepsilon$ and $d(y,z)<\varepsilon$. Then
$$
d(w,z)\le d(w,x)+d(x,y)+d(y,z)<r+2\varepsilon<b,
$$
and from $d(x,y)\le d(x,w)+d(w,z)+d(z,y)$,
$$
a<r-2\varepsilon=d(x,y)-d(x,w)-d(y,z)\le d(w,z).
$$
So $a<d(w,z)<b$ and $w\times z\in d^{-1}((a,b))$. Hence the inverse image is open and $d$ is continuous.

(b) If $d:X'\times X'\to\RR$ is continuous then, for fixed $x\in X'$, the map $h(y)=d(x,y)$ is continuous on $X'$ (it is $d$ composed with the imbedding $y\mapsto x\times y$, Exercise 18.4). For $\varepsilon>0$,
$$
B_{d}(x,\varepsilon)=\{y\in X'\mid d(x,y)<\varepsilon\}=h^{-1}((-\infty,\varepsilon))
$$
is open in $X'$. As the $d$-balls form a basis for the topology of $X$, the topology of $X'$ contains that basis and is therefore finer than the topology of $X$. So the topology induced by $d$ is the coarsest topology on $X$ for which $d$ is continuous.
:::
