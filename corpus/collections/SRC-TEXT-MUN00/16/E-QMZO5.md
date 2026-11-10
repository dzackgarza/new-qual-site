---
schema: qual/card@1
id: E-QMZO5
kind: problem
title: Dictionary order topology on the plane as a product topology
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 9, printed p. 92; the stored
    statement is the printed one, R_d being R with the discrete topology.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 16.9, PDF p. 5. Both inclusions are his: {a} x
    (b,d) is a dictionary-open interval, and an interval ((a,b),(c,d)) with a < c is the
    union of {a} x (b,infinity), (a,c) x R and {c} x (-infinity,d), each a union of product
    basis elements. Strictness over the standard topology of R^2 is his witness {0} x (0,1).
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Show that the dictionary order topology on the set $\RR \times \RR$ is the same as the product topology $\RR_d \times \RR$, where $\RR_d$ denotes $\RR$ in the discrete topology.
Compare this topology with the standard topology on $\RR^2$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 16.9, PDF p. 5** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the two inclusions and the strictness with the standard topology are his, written out below with the decomposition spelled out. Whitman's answer on printed pp. 155--156 is the same.

Let $\mathcal{T}_{d}$ be the dictionary order topology on $\RR\times\RR$ and $\mathcal{T}_{p}$ the product topology on $\RR_{d}\times\RR$, where $\RR_{d}$ is $\RR$ with the discrete topology.

*$\mathcal{T}_{p}\subset\mathcal{T}_{d}$.* A basis element of $\mathcal{T}_{p}$ is $\{a\}\times(b,d)$ with $a,b,d\in\RR$, $b<d$. This is the set of points $(x,y)$ with $(a,b)\prec(x,y)\prec(a,d)$, an open interval in the dictionary order, hence a basis element of $\mathcal{T}_{d}$.

*$\mathcal{T}_{d}\subset\mathcal{T}_{p}$.* The dictionary order on $\RR\times\RR$ has no smallest and no largest element, so a basis element of $\mathcal{T}_{d}$ is an interval $\big((a,b),(c,d)\big)$ with $(a,b)\prec(c,d)$. If $a=c$ it is $\{a\}\times(b,d)$, which is a basis element of $\mathcal{T}_{p}$. If $a<c$, then
$$
\big((a,b),(c,d)\big)
=\big(\{a\}\times(b,\infty)\big)\cup\big((a,c)\times\RR\big)\cup\big(\{c\}\times(-\infty,d)\big),
$$
as the dictionary order compares first coordinates first: the points above $(a,b)$ and below $(c,d)$ are those with $a<x<c$, together with those with $x=a$ and $y>b$ and those with $x=c$ and $y<d$. Each of the three sets on the right is a union of basis elements of $\mathcal{T}_{p}$,
$$
\{a\}\times(b,\infty)=\bigcup_{r>b}\{a\}\times(b,r),\quad
(a,c)\times\RR=\bigcup_{a<t<c}\bigcup_{s<r}\{t\}\times(s,r),\quad
\{c\}\times(-\infty,d)=\bigcup_{s<d}\{c\}\times(s,d),
$$
so the interval lies in $\mathcal{T}_{p}$. Hence $\mathcal{T}_{d}=\mathcal{T}_{p}$.

*Comparison with the standard topology.* Let $\mathcal{T}$ be the standard topology on $\RR^{2}$. Then $\mathcal{T}\subset\mathcal{T}_{p}$: a basis element $(a,b)\times(c,d)$ of $\mathcal{T}$ is $\bigcup_{a<t<b}\{t\}\times(c,d)$, a union of basis elements of $\mathcal{T}_{p}$. The inclusion is strict: $\{0\}\times(0,1)$ is a basis element of $\mathcal{T}_{p}$, but it is not open in the standard topology, since every standard basis element containing $(0,1/2)$ contains points with first coordinate $\ne0$. So $\mathcal{T}_{d}=\mathcal{T}_{p}$ is strictly finer than the standard topology on $\RR^{2}$.
:::
